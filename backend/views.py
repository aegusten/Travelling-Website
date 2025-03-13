import json
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

from backend.core.models import CustomUser, Country
from .forms import UserRegistrationForm, AdvancedSearchForm
from backend.core.service import get_visa_recommendations, get_budget_recommendations

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'utils/profile.html')


@login_required
def profile_update(request):
    if request.headers.get('Content-Type') == 'application/json':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        update_type = data.get('update_type', '')

        if update_type == "country":
            typed_country = data.get('country', '').strip()
            if not typed_country:
                return JsonResponse({"error": "No country provided"}, status=400)

            try:
                country_obj = Country.objects.get(country_name__iexact=typed_country)
                request.user.country = country_obj
                request.user.save()
                return JsonResponse({"success": True, "message": "Country updated"})
            except Country.DoesNotExist:
                return JsonResponse({
                    "error": "No matching country found for: " + typed_country
                }, status=400)

        elif update_type == "currency":
            typed_currency = data.get('currency', '').strip()
            if not typed_currency:
                return JsonResponse({"error": "No currency provided"}, status=400)

            found = Country.objects.filter(currency_code__iexact=typed_currency).exists()
            if not found:
                return JsonResponse({
                    "error": "No matching currency found for: " + typed_currency
                }, status=400)

            request.user.currency = typed_currency
            request.user.save()
            return JsonResponse({"success": True, "message": "Currency updated"})

        return JsonResponse({"error": "Unknown update_type"}, status=400)

    if request.method == 'POST':
        update_type = request.POST.get('update_type')
        if update_type == 'email':
            request.user.email = request.POST.get('email', '')
            request.user.save()
            messages.success(request, "Email updated successfully.")
        elif update_type == 'username':
            request.user.username = request.POST.get('username', '')
            request.user.save()
            messages.success(request, "Username updated successfully.")
        elif update_type == 'password':
            new_password = request.POST.get('password', '')
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, "Password updated successfully.")
        return redirect('profile')

    return redirect('profile')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'index.html', {'form': form})

@login_required
def travel_recommendations(request):
    user = request.user
    if not user.country:
        return render(request, 'dashboard/no_passport.html')
    visa_toggle = request.GET.get('visa', 'on')
    budget_toggle = request.GET.get('budget', 'on')
    destination = request.GET.get('destination', None)
    if user.budget:
        budget_value = user.budget
    else:
        budget_value = request.GET.get('budget_value', 3000)
    visa_data = None
    budget_data = None
    if visa_toggle == 'on':
        visa_data = get_visa_recommendations(user.country.name)
    if budget_toggle == 'on' and destination:
        budget_data = get_budget_recommendations(budget_value, destination)
    context = {
        'visa_data': visa_data,
        'budget_data': budget_data,
        'budget_value': budget_value,
        'destination': destination,
    }
    return render(request, 'dashboard/recommendations.html', context)