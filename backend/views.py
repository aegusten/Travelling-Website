import json
from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils.text import slugify
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import pprint

from backend.core.models import CustomUser, Country
from .forms import UserRegistrationForm, AdvancedSearchForm
from .services import (
    fetch_hotels,
    fetch_events,
    get_transport_food_cost,
    get_visa_info,
    fetch_destination_locations,
    fetch_destination_currency,
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
                return JsonResponse({"error": f"No matching country found for: {typed_country}"}, status=400)

        elif update_type == "currency":
            typed_currency = data.get('currency', '').strip()
            if not typed_currency:
                return JsonResponse({"error": "No currency provided"}, status=400)
            if not Country.objects.filter(currency_code__iexact=typed_currency).exists():
                return JsonResponse({"error": f"No matching currency found for: {typed_currency}"}, status=400)
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
    return render(request, "index.html", {"form": form})


@csrf_exempt
def search_view(request):
    dest = request.GET.get("destination", "").strip()
    try:
        pax = int(request.GET.get("pax", "1") or 1)
    except ValueError:
        pax = 1
    try:
        days = int(request.GET.get("days", "1") or 1)
    except ValueError:
        days = 1

    budget_str = request.GET.get("budget", "").strip()
    user_currency = request.GET.get("currency", "").strip() or "USD"
    visa_enabled = request.GET.get("visa_enabled") == "on"

    try:
        budget = Decimal(budget_str) if budget_str else None
    except Exception:
        budget = None

    user = request.user if request.user.is_authenticated else None
    if not user:
        budget = None
        visa_enabled = False

    passport_country = user.country.country_name if (user and user.country and visa_enabled) else None
    locs = fetch_destination_locations(dest)
    if not locs:
        locs = [{"cityName": dest, "reason": f"Explore {dest}", "country": dest}]

    first_loc = locs[0]
    destination_country = first_loc.get("country", "")
    is_country = (destination_country.lower() == dest.lower())
    relevant_locs = locs[:3] if is_country else [first_loc]

    visa_info = get_visa_info(passport_country, destination_country) if passport_country else None
    short_visa = visa_info["short_visa"] if visa_info else "Unknown"

    results = []
    for loc in relevant_locs:
        city_name = loc.get("cityName", "Unknown")
        country_name = loc.get("country", destination_country) or "Unknown"
        hotels = fetch_hotels(city_name, user_currency, limit=3, days=days) if not is_country else []
        events = fetch_events(city_name, user_currency, limit=3) if not is_country else []
        cost_data = get_transport_food_cost(city_name, pax, days)

        # Calculate average hotel cost if available
        if hotels:
            avg_hotel_cost = sum(hotel["price"] for hotel in hotels) / len(hotels)
        else:
            avg_hotel_cost = 0

        # Calculate average event cost if available
        if events:
            avg_event_cost = sum(event["price"] for event in events) / len(events)
        else:
            avg_event_cost = 0

        # Total estimated cost includes mid-range transport/food plus average hotel and event costs
        total_cost = cost_data["total_cost"]["mid_range"] + avg_hotel_cost + avg_event_cost
        final_cost = fetch_destination_currency(total_cost, "USD", user_currency) if user_currency else total_cost

        detail_url = reverse("destination_detail", kwargs={"slug": slugify(city_name)})
        # Debug: Print the generated detail URL for each result
        print(f"DEBUG: Generated detail_url for {city_name} -> {detail_url}")

        result = {
            "place_name": city_name,
            "destination": country_name,
            "days": days,
            "pax": pax,
            "budget": str(budget) if budget else None,
            "currency": user_currency,
            "destination_currency": user_currency,
            "cost_in_destination_currency": final_cost,
            "converted_cost": final_cost,
            "cost_text": f"{final_cost} {user_currency}",
            "image_url": "/static/images/default-city.jpg",
            "description": loc.get("reason") or f"Explore {city_name}, part of {country_name}",
            "detail_url": detail_url,
            "hotels": hotels,
            "events": events,
            "transport_cost": cost_data.get("transport", {}),
            "food_cost": cost_data.get("food", {}),
            "short_visa": short_visa,
            "visa_text": visa_info,
        }
        results.append(result)

    # Debug: Print entire results structure
    print("DEBUG: Search results:")
    pprint.pprint(results)

    request.session["search_results"] = results
    return render(request, "search_results.html", {"searched": True, "results": results})

@csrf_exempt
def destination_detail(request, slug):
    stored = request.session.get("search_results", [])
    # Debug: Print stored session data
    print("DEBUG: Stored search_results from session:")
    pprint.pprint(stored)
    # Debug: Print the requested slug
    print("DEBUG: Requested slug:", slug)
    
    dest_obj = next((x for x in stored if slugify(x["place_name"]) == slug), None)
    # Debug: Print the found destination object
    print("DEBUG: Found destination object:", dest_obj)
    
    if not dest_obj:
        print("DEBUG: Available slugs in session:")
        for item in stored:
            print(slugify(item["place_name"]))
        return render(request, "not_found.html", {"message": "Destination not found."})
    return render(request, "details.html", {"destination": dest_obj})