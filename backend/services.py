import os
import openai
import json
import re
from dotenv import load_dotenv
from pathlib import Path
from backend.core.models import Country

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

openai.api_key = "KEY_HERE"

print("DEBUG: OPENAI KEY =", openai.api_key)
if not openai.api_key:
    print("❌ GPT API KEY not loaded!")
else:
    print("✅ GPT API KEY loaded successfully.")

def ask_gpt(prompt, system_role="You are a helpful travel assistant"):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("GPT Error:", e)
        return None

def fetch_destination_locations(destination):
    is_country = Country.objects.filter(country_name__iexact=destination.strip()).exists()

    if is_country:
        prompt = (
            f"List 3 major cities or tourist areas in {destination}. "
            "Format: City: Brief description"
        )
    else:
        prompt = (
            f"What country is {destination} located in? Also provide a brief description "
            f"of why {destination} is popular. Format: {destination} | Description (Country: CountryName)"
        )

    response = ask_gpt(prompt)
    results = []

    if response:
        lines = response.split("\n")
        for line in lines:
            line = line.strip()
            if line:
                if "|" in line:
                    parts = line.split("|")
                else:
                    parts = line.split(":")
                if len(parts) >= 2:
                    city = parts[0].strip()
                    description = parts[1].strip()
                    country_match = re.search(r"\(Country:\s*(.*?)\)", description)
                    country_name = country_match.group(1).strip() if country_match else destination
                    description_clean = re.sub(r"\(Country:.*?\)", "", description).strip()
                    results.append({
                        "cityName": city,
                        "reason": description_clean,
                        "country": country_name
                    })
    if not results:
        results = [{"cityName": destination, "reason": f"Explore {destination}", "country": destination}]
    return results[:3]

def fetch_hotels(city, user_currency="USD", limit=3, days=1):
    prompt = (
        f"Provide {limit} recommended hotels in {city} with the following details:\n"
        f"- Name\n- Short description\n- Price per night in {user_currency}\n- Rating out of 5\n"
        "Format: Hotel Name | Description | Price | Stars"
    )
    response = ask_gpt(prompt)
    print(f"\nGPT Hotel RAW RESPONSE for {city}:\n{response}\n")

    hotels = []
    if response:
        lines = response.strip().split("\n")
        for line in lines:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 4:
                print(f" Skipped malformed hotel line (not enough parts): {line}")
                continue

            name, desc, price_str, rating = parts[:4]

            if not name or not desc or not price_str or not rating:
                print(f"Skipped hotel due to missing fields: {line}")
                continue

            price_cleaned = re.sub(r"[^\d.]", "", price_str)
            try:
                price_value = float(price_cleaned)
            except:
                print(f" Invalid price format in: {line}")
                continue

            hotels.append({
                "name": name,
                "description": desc,
                "price": round(price_value * days, 2),
                "rating": rating,
                "image_url": "/static/images/default-hotel.jpg"
            })

    print(f" Parsed {len(hotels)} hotels for {city}")
    return hotels[:limit]

def fetch_events(city, user_currency="USD", limit=3):
    prompt = (
        f"List at least {limit} tourist events or attractions in {city}. Include:\n"
        f"- Name\n- Description\n- Entry price in {user_currency}\n"
        "Format: Name | Description | Price"
    )
    response = ask_gpt(prompt)
    print(f"\nGPT Event RAW RESPONSE for {city}:\n{response}")

    events = []
    if response:
        lines = response.strip().split("\n")
        for line in lines:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 3:
                print(f" Skipped malformed event line (not enough parts): {line}")
                continue

            name, desc, price_str = parts[:3]
            if not name or not desc:
                print(f" Skipped event due to missing fields: {line}")
                continue

            price_match = re.search(r"(\d+(?:\.\d+)?)", price_str)
            if not price_match:
                print(f" Could not extract valid price from: {price_str}, defaulting to 0")
                price_value = 0
            else:
                try:
                    price_value = float(price_match.group(1))
                except:
                    print(f" Price extraction failed for: {line}")
                    price_value = 0

            events.append({
                "name": name,
                "description": desc,
                "price": round(price_value, 2),
                "image_url": "/static/images/default-event.jpg"
            })

    print(f"✅ Parsed {len(events)} events for {city}")
    return events[:limit]


def get_transport_food_cost(city, pax, days, user=None):
    user_currency = "USD"
    if user and hasattr(user, 'currency') and user.currency:
        user_currency = user.currency

    prompt = (
        f"You are a travel budget assistant. Estimate the average DAILY transport and food cost PER PERSON in {city} in {user_currency}. "
        f"Output must be in this exact format: Transport: 10,20,40 | Food: 15,30,60 — where values are low, mid, and high budget ranges.\n"
        f"Do not add any explanation. Do not change format. Just return:\nTransport: x,x,x | Food: x,x,x"
    )

    response = ask_gpt(prompt)
    print(f"GPT RAW RESPONSE for {city}: {response}")

    transport_costs = [5, 15, 50]
    food_costs = [10, 25, 80]

    try:
        if response and "Transport:" in response and "Food:" in response and "|" in response:
            transport_data, food_data = response.split("|")
            transport_costs = [float(x.strip().replace(",", "")) for x in transport_data.split(":")[1].split(",")]
            food_costs = [float(x.strip().replace(",", "")) for x in food_data.split(":")[1].split(",")]

    except Exception as e:
        print("⚠️ Error parsing GPT transport/food costs:", e)

    return {
        "city": city,
        "pax": pax,
        "days": days,
        "transport": {
            "low_budget": transport_costs[0] * pax * days,
            "mid_range": transport_costs[1] * pax * days,
            "luxury": transport_costs[2] * pax * days
        },
        "food": {
            "low_budget": food_costs[0] * pax * days,
            "mid_range": food_costs[1] * pax * days,
            "luxury": food_costs[2] * pax * days
        },
        "total_cost": {
            "low_budget": (transport_costs[0] + food_costs[0]) * pax * days,
            "mid_range": (transport_costs[1] + food_costs[1]) * pax * days,
            "luxury": (transport_costs[2] + food_costs[2]) * pax * days
        }
    }

def get_visa_info(passport_country, destination_country): 
    prompt = (
        f"I am from {passport_country}, visiting {destination_country}. What are the visa requirements? "
        "Return one of: Visa-Free, E-Visa, or Visa Required, then explain."
    )
    response = ask_gpt(prompt)
    summary = "Visa Required"
    if response:
        if "Visa-Free" in response:
            summary = "Visa-Free"
        elif "E-Visa" in response:
            summary = "E-Visa"
    else:
        response = "Visa information is currently unavailable."
    return {
        "short_visa": summary,
        "full_visa_text": response
    }

def fetch_destination_currency(amount, from_cur, to_cur):
    prompt = f"Convert {amount} {from_cur} to {to_cur}. Just return the number."
    response = ask_gpt(prompt, system_role="You are a currency converter. Respond only with the number.")
    match = re.search(r"([\d.,]+)", response)
    if match:
        try:
            return float(match.group(1).replace(",", ""))
        except Exception as e:
            print("Error parsing currency conversion:", e)
    return amount

def fetch_image_url(place_name, context="city"):
    if context.lower() == "country":
        query = f"famous landmarks or iconic views in {place_name}"
    else:
        query = f"best cityscape or iconic view of {place_name} (city)"

    prompt = (
        f"Return a direct royalty-free image URL (Unsplash, Pexels, or Wikimedia) that shows a real and recognizable view of {query}. "
        "Avoid abstract or symbolic art. Do not add any text. Just return the clean image URL only."
    )

    response = ask_gpt(prompt, system_role="You are a travel image assistant. Respond only with a usable direct image link, no text or explanation.")

    if response and response.strip().startswith("http"):
        return response.strip()
    else:
        print(f"Invalid or missing image URL from GPT for {place_name}: {response}")
        return "/static/images/default-city.jpg"

def is_image_valid(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200 and 'image' in response.headers.get('Content-Type', '')
    except:
        return False