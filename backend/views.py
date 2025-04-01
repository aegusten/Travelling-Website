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
    fetch_image_url,
    is_image_valid,
)

@csrf_protect
def home_view(request):
    form = AdvancedSearchForm(user=request.user)
    return render(request, "base.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            return render(request, "base.html", {
                "login_form": form,
                "reg_form": UserRegistrationForm(),
            })
    else:
        return redirect("home")
    
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
    return render(request, 'base.html', {'form': form})
 
@csrf_exempt
def destination_detail(request, slug):
    stored = request.session.get("search_results", [])
    print("DEBUG: Stored search_results from session:")
    pprint.pprint(stored)
    print("DEBUG: Requested slug:", slug)
    
    dest_obj = next((x for x in stored if slugify(x["place_name"]) == slug), None)
    print("DEBUG: Found destination object:", dest_obj)
    
    if not dest_obj:
        print("DEBUG: Available slugs in session:")
        for item in stored:
            print(slugify(item["place_name"]))
        return render(request, "not_found.html", {"message": "Destination not found."})

    transport_cost = dest_obj.get('transport_cost', {})
    mid_range = transport_cost.get('mid_range')
    pax = dest_obj.get('pax')
    if mid_range is not None and pax is not None:
        try:
            transport_cost_per_person = float(mid_range) / float(pax)
        except (ValueError, ZeroDivisionError):
            transport_cost_per_person = None
    else:
        transport_cost_per_person = None

    food_cost = dest_obj.get('food_cost', {})
    food_mid_range = food_cost.get('mid_range')
    days = dest_obj.get('days')
    if food_mid_range is not None and days is not None:
        try:
            food_cost_per_day = float(food_mid_range) / float(days)
        except (ValueError, ZeroDivisionError):
            food_cost_per_day = None
    else:
        food_cost_per_day = None
    
    hotels = dest_obj.get('hotels', [])
    hotel_total = 0
    if hotels:
        try:
            hotel_total = sum(float(hotel.get('price', 0)) for hotel in hotels if hotel.get('price') is not None)
        except (ValueError, TypeError):
            hotel_total = 0
    
    events = dest_obj.get('events', [])
    events_total = 0
    if events:
        try:
            events_total = sum(float(event.get('price', 0)) for event in events if event.get('price') is not None)
        except (ValueError, TypeError):
            events_total = 0
    
    return render(request, "details.html", {
        "destination": dest_obj,
        "transport_cost_per_person": transport_cost_per_person,
        "food_cost_per_day": food_cost_per_day,
        "hotel_total": hotel_total,
        "events_total": events_total
    })

@csrf_exempt
def search_view(request):
    try:
        dest = request.GET.get("destination", "").strip()
        print(f"🔍 Destination input: {dest}")

        pax = int(request.GET.get("pax", "1") or 1) if request.GET.get("pax", "1").isdigit() else 1
        days = int(request.GET.get("days", "1") or 1) if request.GET.get("days", "1").isdigit() else 1
        print(f"👥 Pax: {pax}, 🕒 Days: {days}")

        budget_str = request.GET.get("budget", "").strip()
        user_currency = request.GET.get("currency", "").strip() or "USD"
        visa_enabled = request.GET.get("visa_enabled") == "on"
        print(f"💰 Budget input: {budget_str}, Currency: {user_currency}, Visa Enabled: {visa_enabled}")

        budget = Decimal(budget_str) if budget_str else None
        user = request.user if request.user.is_authenticated else None
        if not user:
            print("⚠️ User not authenticated. Ignoring budget and visa.")
            budget = None
            visa_enabled = False
        elif not user.country:
            print("⚠️ User has no country set. Disabling visa feature.")
            visa_enabled = False

        passport_country = user.country.country_name if (user and user.country and visa_enabled) else None
        print(f"🛂 Passport Country: {passport_country}")

        locs = fetch_destination_locations(dest)
        if not locs:
            print("⚠️ No locations found. Falling back to default.")
            locs = [{"cityName": dest, "reason": f"Explore {dest}", "country": dest}]
        print("📍 Locations fetched:", locs)

        first_loc = locs[0]
        destination_country = first_loc.get("country", "")
        print(f"🌍 Destination country detected: {destination_country}")

        destination_currency = "USD"
        try:
            country_obj = Country.objects.filter(country_name__iexact=destination_country).first()
            if country_obj and country_obj.currency_code:
                destination_currency = country_obj.currency_code
            else:
                print(f"⚠️ Currency missing for {destination_country}. Defaulting to USD.")
        except Exception as e:
            print(f"⚠️ Error fetching currency for {destination_country}: {e}")

        is_country = (destination_country.lower() == dest.lower())
        relevant_locs = locs[:3] if is_country else [first_loc]
        visa_info = get_visa_info(passport_country, destination_country) if passport_country else {}
        short_visa = visa_info.get("short_visa")

        results = []
        for loc in relevant_locs:
            city_name = loc.get("cityName") or dest
            if city_name.lower() in ["city", "tourist area", "description"] or city_name.lower().startswith("1."):
                city_name = dest
            print(f"\n🏙️ Processing location: {city_name}")

            country_name = loc.get("country", destination_country)
            hotels = fetch_hotels(city_name, user_currency, limit=3, days=days)
            print("🏨 Hotels fetched")
            events = fetch_events(city_name, user_currency, limit=3)
            print("🎉 Events fetched")

            cost_data = get_transport_food_cost(city_name, pax=pax, days=days, user=user)
            transport_mid = cost_data["transport"]["mid_range"]
            food_mid = cost_data["food"]["mid_range"]
            total_mid_cost = transport_mid + food_mid

            sorted_hotels = sorted(hotels, key=lambda h: h["price"]) if hotels else []
            mid_hotel_price = sorted_hotels[len(sorted_hotels) // 2]["price"] if sorted_hotels else 0

            total_event_price = sum(e["price"] for e in events)

            total_cost = total_mid_cost + mid_hotel_price + total_event_price
            print(f"💰 Total cost in {user_currency}: {total_cost}")

            cost_in_destination_currency = fetch_destination_currency(total_cost, user_currency, destination_currency)
            converted_cost = total_cost

            for hotel in hotels:
                hotel["price_converted"] = fetch_destination_currency(hotel["price"], user_currency, destination_currency)
            for event in events:
                event["price_converted"] = fetch_destination_currency(event["price"], user_currency, destination_currency)
            transport_mid_dest = fetch_destination_currency(transport_mid, user_currency, destination_currency)
            food_mid_dest = fetch_destination_currency(food_mid, user_currency, destination_currency)

            image_url = fetch_image_url(city_name)
            if not is_image_valid(image_url):
                image_url = None
            print("🖼️ Image URL fetched:", image_url)

            if budget is not None:
                try:
                    if converted_cost > float(budget):
                        print(f"⛔ Skipping {city_name} — Budget exceeded ({converted_cost} > {budget})")
                        continue
                except Exception as e:
                    print(f"⚠️ Budget comparison failed: {e}")

            try:
                detail_url = reverse("destination_detail", kwargs={"slug": slugify(city_name)})
            except Exception as e:
                print(f"⚠️ Failed to generate detail URL: {e}")
                detail_url = "#"

            print(f"✅ Adding result: {city_name} → {detail_url}")
            results.append({
                "place_name": city_name,
                "destination": country_name,
                "days": days,
                "pax": pax,
                "budget": str(budget) if budget else None,
                "currency": user_currency,
                "destination_currency": destination_currency,
                "cost_in_destination_currency": cost_in_destination_currency,
                "converted_cost": converted_cost,
                "cost_text": f"{cost_in_destination_currency} {destination_currency} (~ {converted_cost} {user_currency})",
                "image_url": image_url,
                "description": loc.get("reason") or f"Explore {city_name}, part of {country_name}",
                "detail_url": detail_url,
                "hotels": hotels,
                "events": events,
                "transport_cost": {"mid_range": transport_mid, "mid_range_dest": transport_mid_dest},
                "food_cost": {"mid_range": food_mid, "mid_range_dest": food_mid_dest},
                "short_visa": short_visa,
                "visa_text": visa_info,
            })

        print("🎯 Final Results:")
        pprint.pprint(results)

        for idx, res in enumerate(results):
            print(f"\n✅ Result {idx+1} contains:")
            print("🥇 Keys:", list(res.keys()))
            print("📌 Hotels:", res.get("hotels"))
            print("📌 Events:", res.get("events"))
            print("💰 Converted cost:", res.get("converted_cost"))
            print("🌐 URL:", res.get("detail_url"))

        print("📦 Validating session data")
        json.dumps(results)
        print("✅ Results are JSON-serializable")
        request.session["search_results"] = results
        print("✅ Saved to session successfully")

        print("🎨 Rendering template")
        return render(request, "search_results.html", {
            "searched": True,
            "results": results
        })

    except Exception as e:
        import traceback
        print("❌ ERROR IN SEARCH VIEW:", e)
        traceback.print_exc()
        return JsonResponse({"error": "Server error", "details": str(e)}, status=500)