import json
from decimal import Decimal
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
    fetch_hotels,
    fetch_events,
    get_transport_food_cost,
    get_visa_info,
    convert_currency,
    fetch_image,
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


@csrf_exempt
def search_view(request):
    dest = request.GET.get("destination", "").strip()
    pax_str = request.GET.get("people", "1").strip()
    days_str = request.GET.get("days", "1").strip()
    budget_str = request.GET.get("budget", "").strip()
    user_currency = request.GET.get("currency", "").strip()
    visa_enabled = (request.GET.get("visa_enabled") == "on")

    if not dest or not pax_str:
        return render(request, "search_results.html", {"searched": False})

    try:
        pax = int(pax_str)
    except:
        pax = 1
    try:
        days = int(days_str)
    except:
        days = 1
    try:
        budget = Decimal(budget_str) if budget_str else None
    except:
        budget = None

    user = request.user if request.user.is_authenticated else None
    if not user:
        budget = None
        visa_enabled = False

    passport_country = user.country.country_name if (user and user.country and visa_enabled) else None

    locs = fetch_destination_locations(dest) or []
    if not locs:
        locs = [{"cityName": dest, "country": dest}]

    first_loc = locs[0]
    cty = first_loc.get("cityName", "")
    ctry = first_loc.get("country", "")
    is_country = (ctry.lower() == dest.lower())
    relevant_locs = locs[:3] if is_country else [first_loc]

    try:
        visa_info = get_visa_info(passport_country, ctry) if passport_country else None
    except:
        visa_info = None
    short_visa = visa_info["short_visa"] if visa_info else "Unknown"

    results = []
    for loc in relevant_locs:
        city_name = loc.get("cityName", "Unknown")
        country_name = loc.get("country", "Unknown")

        hotels = fetch_hotels(city_name, user_currency, limit=2)
        events = fetch_events(city_name, user_currency, limit=3)

        base_cost = 100 * pax * days
        try:
            tc = get_transport_food_cost(city_name, pax, days)
            base_cost = tc["total_cost"]["mid_range"]
        except:
            tc = {}

        if user_currency:
            gpt_converted = fetch_destination_currency(base_cost, "USD", user_currency)
            if gpt_converted is None:
                print("WARNING: GPT failed to convert currency, using base cost instead.")
                final_cost = base_cost
            else:
                final_cost = gpt_converted

        else:
            final_cost = base_cost

        r = {
            "place_name": city_name,
            "destination": country_name,
            "days": days,
            "pax": pax,
            "budget": str(budget) if budget else None,
            "currency": user_currency or "USD",
            "destination_currency": user_currency or "USD",
            "cost_in_destination_currency": final_cost,
            "converted_cost": final_cost,
            "cost_text": f"{final_cost} {user_currency or 'USD'}",
            "image_url": fetch_image(city_name),
            "description": f"Explore {city_name}, part of {country_name}",
            "detail_url": reverse("destination_detail", kwargs={"slug": slugify(city_name)}),
            "hotels": hotels,
            "events": events,
            "transport_cost": tc.get("transport", {}),
            "food_cost": tc.get("food", {}),
            "short_visa": short_visa,
            "visa_text": visa_info,
        }
        results.append(r)

    request.session["search_results"] = results
    return render(request, "search_results.html", {"searched": True, "results": results})


@csrf_exempt
def destination_detail(request, slug):
    stored = request.session.get("search_results", [])
    dest_obj = next((x for x in stored if slugify(x["place_name"]) == slug), None)

    if not dest_obj:
        return render(request, "not_found.html", {"message": "Destination not found."})

    return render(request, "details.html", {"destination": dest_obj})