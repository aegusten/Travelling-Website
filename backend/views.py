import json
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from backend.core.models import CustomUser, Country
from .forms import UserRegistrationForm, AdvancedSearchForm
from backend.core.service import get_visa_recommendations, get_budget_recommendations

from .services import (
    fetch_booking_reviews,
    fetch_airbnb_properties,
    get_visa_requirement,
    convert_currency_http,
    get_budget_recommendations,
)

from decimal import Decimal

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

@csrf_protect
def home_view(request):
    form = AdvancedSearchForm(user=request.user)
    context = {
        "form": form,
    }
    return render(request, "index.html", context)


def country_detail_view(request, country_id):
    """
    If you have a real Country model with an integer PK,
    you can show a full page of details (roadmap).
    """
    # from .models import Country
    # country_obj = get_object_or_404(Country, pk=country_id)
    # hotels = get_hotels_and_places(country_obj.country_name, country_obj.currency_code)
    # ...
    # return render(request, "country_detail.html", {...})
    pass


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
    form_budget_str = request.GET.get("budget", "").strip()
    form_currency = request.GET.get("currency", "").strip()
    visa_enabled = (request.GET.get("visa_enabled") == "on")

    if not destination or not pax_str:
        print("DEBUG: No destination or pax provided -> returning empty snippet.")
        return render(request, "search_results.html", {"searched": False})

    try:
        pax = int(pax_str)
    except:
        pax = 1
    try:
        days = int(days_str) if days_str else None
    except:
        days = None
    try:
        budget = Decimal(form_budget_str) if form_budget_str else None
    except:
        budget = None
    currency = form_currency if form_currency else None

    print(
        "DEBUG: Form data =>",
        f"destination={destination}, pax={pax}, days={days}, budget={budget}, currency={currency}, visa_enabled={visa_enabled}"
    )

    user = request.user if request.user.is_authenticated else None
    passport_country_code = None
    if visa_enabled and user and user.country and user.country.country_code:
        passport_country_code = user.country.country_code.upper()

    airbnb_data = None
    visa_info = None
    extra_data = None

    try:
        airbnb_data = fetch_airbnb_properties(
            location=destination,
            currency=currency if currency else None,
            adults=pax
        )
        print("DEBUG: Airbnb data =>", airbnb_data)
    except Exception as e:
        print("DEBUG: Airbnb call failed =>", e)
        airbnb_data = None

    if visa_enabled and passport_country_code:
        try:
            dest_country_code = destination[:2].upper()
            visa_info = get_visa_requirement(passport_country_code, dest_country_code)
            print("DEBUG: Visa info =>", visa_info)
        except Exception as e:
            print("DEBUG: Visa call failed =>", e)
            visa_info = None

    if budget:
        try:
            extra_data = get_budget_recommendations(budget=budget, additional_context=destination)
            print("DEBUG: Extra data =>", extra_data)
        except Exception as e:
            print("DEBUG: get_budget_recommendations failed =>", e)
            extra_data = None

    results = []
    if airbnb_data and isinstance(airbnb_data, dict):
        data_obj = airbnb_data.get("data", {})
        items = data_obj.get("list", [])
        if not isinstance(items, list):
            items = []
        for item in items[:3]:
            listing = item.get("listing", {})
            pricing = item.get("pricingQuote", {})
            place_name = listing.get("name", f"{destination} Place")
            images = listing.get("contextualPictures", [])
            if images:
                first_image_url = images[0].get("picture", "/static/images/default.jpg")
            else:
                first_image_url = "/static/images/default.jpg"
            structured_price = pricing.get("structuredStayDisplayPrice", {})
            primary_line = structured_price.get("primaryLine", {})
            approx_cost_text = primary_line.get("price", "500")
            item_obj = {
                "place_name": place_name,
                "destination": destination,
                "days": days,
                "pax": pax,
                "budget": str(budget) if budget else None,
                "currency": currency,
                "cost_text": approx_cost_text,
                "image_url": first_image_url,
                "description": listing.get("city", ""),
                "detail_url": f"/country/{listing.get('id', 1)}/",
            }
            if visa_info and isinstance(visa_info, dict) and visa_enabled:
                visa_req = visa_info.get("visa_requirement", "Visa data unavailable")
                item_obj["description"] += f" (Visa Info: {visa_req})"
            results.append(item_obj)

    extra_results = []
    if extra_data and isinstance(extra_data, list):
        for item in extra_data[:2]:
            cost = item.get("estimated_cost", 500)
            extra_results.append({
                "place_name": item.get("destination", "Extra Destination"),
                "days": days,
                "pax": pax,
                "budget": str(budget) if budget else None,
                "currency": currency,
                "cost_text": f"{cost} {currency}" if currency else f"{cost} USD",
                "image_url": item.get("image_url", "/static/images/default.jpg"),
                "description": item.get("description", ""),
                "detail_url": f"/country/{item.get('id', 99)}/",
            })

    print("DEBUG: Final results =>", results)
    print("DEBUG: Final extra_results =>", extra_results)

    context = {
        "searched": True,
        "results": results,
        "extra_results": extra_results,
    }
    return render(request, "search_results.html", context)