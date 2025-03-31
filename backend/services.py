import os
import openai
import json
import re
from dotenv import load_dotenv
from pathlib import Path
from backend.core.models import Country

# Load env vars
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

openai.api_key = os.getenv("OPENAI_API_KEY")

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
    """
    Determines if the provided destination is a country or a city.
    If a country, returns 3 popular cities/tourist areas.
    If a city, returns details including the country it is located in.
    """
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
                # Expecting either "City: Description" or "City | Description (Country: CountryName)"
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
    # Fallback: if no valid response, assume destination is the city and country.
    if not results:
        results = [{"cityName": destination, "reason": f"Explore {destination}", "country": destination}]
    return results[:3]

def fetch_hotels(city, user_currency="USD", limit=3, days=1):
    """
    Fetches hotel recommendations using GPT.
    Returns a list of hotel dictionaries without dynamic image fetching.
    """
    prompt = (
        f"Provide {limit} recommended hotels in {city} with the following details:\n"
        f"- Name\n- Short description\n- Price per night in {user_currency}\n- Rating out of 5\n"
        "Format: Hotel Name | Description | Price | Stars"
    )

    response = ask_gpt(prompt)
    hotels = []

    if response:
        lines = response.split("\n")
        for line in lines:
            parts = line.split("|")
            if len(parts) == 4:
                price_str = parts[2].strip()
                # Clean price string and check if it's empty.
                cleaned_price = re.sub(r"[^\d.]", "", price_str)
                if not cleaned_price:
                    price_value = 100.0
                else:
                    try:
                        price_value = float(cleaned_price)
                    except Exception as e:
                        print("Error parsing hotel price:", e)
                        price_value = 100.0
                hotels.append({
                    "name": parts[0].strip(),
                    "description": parts[1].strip(),
                    "price": round(price_value * days, 2),
                    "rating": parts[3].strip(),
                    "image_url": "/static/images/default-hotel.jpg"
                })

    return hotels[:limit]

def fetch_events(city, user_currency="USD", limit=3):
    """
    Fetches event or attraction recommendations using GPT.
    Returns a list of event dictionaries without dynamic image fetching.
    """
    prompt = (
        f"List {limit} tourist events or attractions in {city}. Include the following details:\n"
        f"- Name\n- Description\n- Entry price in {user_currency}\n"
        "Format: Name | Description | Price"
    )
    response = ask_gpt(prompt)
    events = []

    if response:
        lines = response.split("\n")
        for line in lines:
            parts = line.split("|")
            if len(parts) == 3:
                price_str = parts[2].strip()
                cleaned_price = re.sub(r"[^\d.]", "", price_str)
                if not cleaned_price:
                    event_price = 20.0
                else:
                    try:
                        event_price = float(cleaned_price)
                    except Exception as e:
                        print("Error parsing event price:", e)
                        event_price = 20.0
                events.append({
                    "name": parts[0].strip(),
                    "description": parts[1].strip(),
                    "price": round(event_price, 2),
                    "image_url": "/static/images/default-event.jpg"
                })
    return events

def get_transport_food_cost(city, pax, days, user_currency="USD"):
    """
    Estimates daily transport and food cost per person using GPT.
    Returns costs for low, mid, and luxury budgets.
    """
    prompt = (
        f"Estimate the daily transport and food cost per person in {city} in {user_currency}.\n"
        "Format: Transport: low, mid, high | Food: low, mid, high"
    )
    response = ask_gpt(prompt)
    try:
        transport_data, food_data = response.split(" | ")
        transport_costs = [
            float(x.strip().replace("$", "")) for x in transport_data.split(":")[1].split(",")
        ]
        food_costs = [
            float(x.strip().replace("$", "")) for x in food_data.split(":")[1].split(",")
        ]
    except Exception as e:
        print("Error parsing transport/food costs:", e)
        transport_costs = [5, 15, 50]
        food_costs = [10, 25, 80]

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
    """
    Retrieves visa requirement information using GPT.
    Expects a response that includes one of: Visa-Free, E-Visa, or Visa Required.
    """
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
    """
    Converts a given amount from one currency to another using GPT.
    Expects a response containing only the numeric converted value.
    """
    prompt = f"Convert {amount} {from_cur} to {to_cur}. Just return the number."
    response = ask_gpt(prompt, system_role="You are a currency converter. Respond only with the number.")
    match = re.search(r"([\d.,]+)", response)
    if match:
        try:
            return float(match.group(1).replace(",", ""))
        except Exception as e:
            print("Error parsing currency conversion:", e)
    return amount