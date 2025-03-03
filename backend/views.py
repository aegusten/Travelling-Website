from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from backend.core.models import CustomUser
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from backend.core.service import get_visa_recommendations, get_budget_recommendations


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

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'utils/profile.html')


@login_required
def travel_recommendations(request):
    user = request.user

    if not user.passport_country:
        return render(request, 'dashboard/no_passport.html')  

    visa_toggle = request.GET.get('visa', 'on') 
    budget_toggle = request.GET.get('budget', 'on')  
    budget_value = request.GET.get('budget_value', 3000) 
    destination = request.GET.get('destination', None)

    visa_data = None
    budget_data = None

    if visa_toggle == 'on':
        visa_data = get_visa_recommendations(user.passport_country.name)
    
    if budget_toggle == 'on' and destination:
        budget_data = get_budget_recommendations(budget_value, destination)

    context = {
        'visa_data': visa_data,
        'budget_data': budget_data,
        'budget_value': budget_value,
        'destination': destination,
    }
    return render(request, 'dashboard/recommendations.html', context)