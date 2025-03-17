import json
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.utils.text import slugify
from django.urls import reverse
from decimal import Decimal

from django.views.decorators.csrf import (
    csrf_protect, 
    csrf_exempt,
)

from backend.core.models import (
    CustomUser, 
    Country
)

from .forms import (
    UserRegistrationForm, 
    AdvancedSearchForm
)


from .services import (
    get_visa_requirement_from_chatgpt,
    convert_currency,
    fetch_airbnb_properties,
    get_hotels,
    get_events,
    calculate_total_cost,
    get_popular_destinations,
    fetch_destination_locations,
    get_transport_food_cost,
)



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

@csrf_protect
def home_view(request):
    form = AdvancedSearchForm(user=request.user)
    context = {
        "form": form,
    }
    return render(request, "index.html", context)

def some_login_view(request):

    if request.method == "POST":
        # Make sure your form has {% csrf_token %} in the template
        # or use django’s built-in login 
        pass
    return render(request, "login.html")


@csrf_exempt
def ajax_search_view(request):
    destination = request.GET.get("destination", "").strip()
    pax_str = request.GET.get("people", "").strip()
    days_str = request.GET.get("days", "").strip()
    budget_str = request.GET.get("budget", "").strip()
    currency = request.GET.get("currency", "").strip()
    visa_enabled = request.GET.get("visa_enabled") == "on"

    if not destination or not pax_str:
        return render(request, "search_results.html", {"searched": False})

    try:
        pax = int(pax_str)
    except ValueError:
        pax = 1
    try:
        days = int(days_str) if days_str else 1
    except ValueError:
        days = 1
    try:
        budget = Decimal(budget_str) if budget_str else None
    except:
        budget = None

    user = request.user if request.user.is_authenticated else None
    passport_country_name = None

    if not user:
        budget = None
        visa_enabled = False

    if user and visa_enabled:
        if user.country:
            passport_country_name = user.country.country_name
        else:
            visa_enabled = False

    stored_results = request.session.get("search_results", [])
    if stored_results and stored_results[0]["destination"] == destination:
        return render(request, "search_results.html", {"searched": True, "results": stored_results})

    results = []
    
    locations_data = fetch_destination_locations(destination) or [{"cityName": destination, "country": destination}]

    try:
        visa_info = get_visa_requirement_from_chatgpt(passport_country_name, destination) if visa_enabled and passport_country_name else None
    except Exception as e:
        print(f"DEBUG: Visa API error - {e}")
        visa_info = None

    for location in locations_data[:3]:
        state_or_city_name = location.get("cityName", "Unknown Location")
        country_name = location.get("country", destination)

        hotels = get_hotels(state_or_city_name, currency, limit=2) or []
        events = get_events(state_or_city_name, limit=3) or []
        
        transport_food_cost = {"transport": 50 * pax * days, "food": 30 * pax * days} # Hardcoded transport and food costs

        total_cost = calculate_total_cost(hotels, events, transport_food_cost["transport"], transport_food_cost["food"], days, pax)

        try:
            converted_cost = convert_currency(total_cost, from_cur="USD", to_cur=currency) if currency else total_cost
        except Exception as e:
            print(f"DEBUG: Currency conversion error - {e}")
            converted_cost = total_cost

        result_obj = {
            "place_name": state_or_city_name,
            "destination": country_name,
            "days": days,
            "pax": pax,
            "budget": str(budget) if budget else None,
            "currency": currency or "USD",
            "cost_text": f"{total_cost} USD ({converted_cost} {currency})" if currency else f"{total_cost} USD",
            "image_url": location.get("image_url", "/static/images/default.jpg"),
            "description": f"Explore {state_or_city_name}, a beautiful part of {country_name}.",
            "detail_url": reverse("destination_detail", kwargs={"slug": slugify(state_or_city_name)}),
            "hotels": hotels,
            "events": events,
            "transport_cost": transport_food_cost["transport"],
            "food_cost": transport_food_cost["food"],
        }

        if visa_info:
            result_obj["visa_text"] = visa_info

        results.append(result_obj)

    request.session["search_results"] = results

    return render(request, "search_results.html", {"searched": True, "results": results})

def destination_detail(request, slug):
    stored_results = request.session.get("search_results", [])
    destination = None

    for result in stored_results:
        if slugify(result["place_name"]) == slug:
            destination = result
            break

    if not destination:
        return render(request, "destination_detail.html", {"destination": None})

    return render(request, "destination_detail.html", {"destination": destination})