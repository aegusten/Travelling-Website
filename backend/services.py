import os
import json
import openai
import requests
import urllib.parse
import http.client
import datetime
import logging
import re

api_logger = logging.getLogger(__name__)

api_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler.setFormatter(formatter)
api_logger.addHandler(handler)

RAPIDAPI_KEY = "fafe86aa08mshe186c948008269cp11ea81jsn8f787af70a3d"
OPENAI_API_KEY = "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"
UNSPLASH_ACCESS_KEY = "a0B_rrGB_a9vQhLAQBWuKM7ztE6mJ3Jp4NMxSdyvedM"
UNSPLASH_SECRET_KEY = "eTBMXThIs3-UjN_7E0AZuUlAr5z0m3s6zswa7yO2ShE"

openai.api_key = OPENAI_API_KEY


def get_user_input():
    return {
        "destination": input("Enter Destination: "),
        "pax": int(input("Enter number of people: ")),
        "days": int(input("Enter number of days: ")),
        "budget": float(input("Enter your budget: ")),
        "currency": input("Enter currency (USD, EUR, etc.): ").upper(),
        "visa_enabled": input("Do you need visa information? (yes/no): ").strip().lower() == "yes"
    }


def convert_currency(amount, from_cur, to_cur):
    if not amount or amount <= 0:
        api_logger.warning(f"Invalid amount for conversion: {amount}")
        return amount

    conn = http.client.HTTPSConnection("currency-conversion-and-exchange-rates.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }
    url = f"/convert?from={from_cur}&to={to_cur}&amount={amount}"

    api_logger.debug(f"Requesting Currency Conversion: {url}")

    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    
    # Log the raw response from the currency conversion API
    print("DEBUG: convert_currency raw response:", data.decode("utf-8"))
    
    try:
        response_json = json.loads(data.decode("utf-8"))
        api_logger.debug(f"convert_currency raw response: {json.dumps(response_json, indent=2)}")

        if response_json.get("success"):
            return response_json.get("result", amount)
        else:
            api_logger.error(f"convert_currency error: {response_json}")
            return amount 
    except Exception as e:
        api_logger.error(f"convert_currency failed: {e}")
        return amount


def fetch_hotels(city, user_currency, limit=2, destination_currency="USD"):
    conn = http.client.HTTPSConnection("airbnb19.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "airbnb19.p.rapidapi.com"
    }
    encoded_city = urllib.parse.quote(city)
    url = f"/api/v1/searchPropertyByLocationV2?location={encoded_city}&totalRecords={limit}&currency=USD&adults=1"
    api_logger.debug(f"Requesting Hotels: {url}")
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    print("DEBUG: fetch_hotels raw response:", data.decode("utf-8"))

    hotel_list = []
    
    try:
        js = json.loads(data.decode("utf-8"))
        hotel_list = js.get("data", {}).get("list", [])
    except:
        pass

    output = []
    for h in hotel_list:
        price = h.get("price")
        if price is None:
            price = "Price Not Available"
        else:
            original_cur = h.get("currency", "USD")
            price = convert_currency(price, original_cur, user_currency) if user_currency else price

        output.append({
            "name": h.get("name", "Unknown"),
            "description": h.get("description", ""),
            "image_url": h.get("image_url", fetch_image(city)),
            "price": f"{price} {user_currency}" if user_currency else f"{price} {original_cur}",
            "rating": h.get("rating", "N/A"),
            "amenities": h.get("amenities", "N/A"),
        })

    return output



def fetch_events(city, user_currency, limit=3):
    conn = http.client.HTTPSConnection("booking-com15.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "booking-com15.p.rapidapi.com"
    }
    encoded_city = urllib.parse.quote(city)
    url = f"/api/v1/attraction/searchAttractions?id={encoded_city}&sortBy=trending&page=1&languagecode=en-us"

    api_logger.debug(f"Requesting Events: {url}")
    
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    print("DEBUG: fetch_events raw response:", data.decode("utf-8"))

    try:
        response_json = json.loads(data.decode("utf-8"))

        if not response_json.get("status"): 
            api_logger.error(f"fetch_events error: {response_json.get('message', 'Unknown error')}")
            return []  

        event_list = response_json.get("data", {}).get("products", [])

        output = []
        for e in event_list[:limit]:
            amt = e.get("representativePrice", {}).get("amount", 0)
            orig_cur = e.get("representativePrice", {}).get("currencyCode", "USD")
            if user_currency:
                conv_amt = convert_currency(amt, orig_cur, user_currency)
                show_amt = f"{conv_amt} {user_currency}"
            else:
                show_amt = f"{amt} {orig_cur}"

            output.append({
                "name": e.get("name", "Unknown"),
                "description": e.get("shortDescription", ""),
                "image_url": e.get("primaryPhoto", {}).get("url", fetch_image(city)),
                "price": show_amt,
            })
        
        return output
    
    except json.JSONDecodeError as e:
        api_logger.error(f"fetch_events JSON parsing error: {e}")
        return []


def get_transport_food_cost(city, pax, days):
    prompt = f"""
    Estimate the daily transport and food cost per person in {city}.
    - Transport: Provide low-budget, mid-range, and high-end prices.
    - Food: Provide low-budget, mid-range, and high-end prices.
    - Currency: USD.
    - Format: "Transport: low, mid, high | Food: low, mid, high".
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert travel cost estimator."},
                  {"role": "user", "content": prompt}]
    )

    cost_info = response.choices[0].message.content.strip()
    
    print("DEBUG: get_transport_food_cost raw response:", cost_info)

    try:
        transport_data, food_data = cost_info.split(" | ")
        transport_low, transport_mid, transport_high = [float(x.replace("$", "").strip()) for x in transport_data.split(": ")[1].split(",")]
        food_low, food_mid, food_high = [float(x.replace("$", "").strip()) for x in food_data.split(": ")[1].split(",")]
    except Exception as e:
        print("DEBUG: get_transport_food_cost error parsing costs:", e)
        transport_low, transport_mid, transport_high = 5, 15, 50
        food_low, food_mid, food_high = 10, 25, 80

    return {
        "city": city,
        "pax": pax,
        "days": days,
        "transport": {
            "low_budget": transport_low * pax * days,
            "mid_range": transport_mid * pax * days,
            "luxury": transport_high * pax * days
        },
        "food": {
            "low_budget": food_low * pax * days,
            "mid_range": food_mid * pax * days,
            "luxury": food_high * pax * days
        },
        "total_cost": {
            "low_budget": (transport_low + food_low) * pax * days,
            "mid_range": (transport_mid + food_mid) * pax * days,
            "luxury": (transport_high + food_high) * pax * days
        }
    }


def get_visa_info(passport_country, destination_country):
    prompt = f"I am a traveler from {passport_country} planning to visit {destination_country}. What are the visa requirements? Provide a one-word summary: 'Visa-Free', 'E-Visa', or 'Visa Required', then give full details."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    visa_text = response["choices"][0]["message"]["content"].strip()
    
    # Log the raw response from OpenAI for visa information
    print("DEBUG: get_visa_info raw response:", visa_text)

    short_visa_type = None

    if "Visa-Free" in visa_text:
        short_visa_type = "Visa-Free"
    elif "E-Visa" in visa_text:
        short_visa_type = "E-Visa"
    elif "Visa Required" in visa_text:
        short_visa_type = "Visa Required"
    
    return {
        "short_visa": short_visa_type,
        "full_visa_text": visa_text
    }


def fetch_image(query):
    url = f"https://api.unsplash.com/photos/random?query={query} travel landmark&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)

    try:
        data = response.json()
        print("DEBUG: fetch_image raw response:", json.dumps(data))

        if "urls" in data:
            return data["urls"].get("regular", "/static/images/default.jpg")
        else:
            return "/static/images/default.jpg"

    except Exception as e:
        print(f"ERROR: Failed to fetch Unsplash image - {e}")
        return "/static/images/default.jpg"



def fetch_destination_locations(destination):
    conn = http.client.HTTPSConnection("booking-com15.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "booking-com15.p.rapidapi.com"
    }

    url = f"/api/v1/attraction/searchLocation?query={urllib.parse.quote(destination)}&languagecode=en-us"
    
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    # Log the raw response from the destination locations API
    print("DEBUG: fetch_destination_locations raw response:", data.decode("utf-8"))
    
    try:
        parsed = json.loads(data.decode("utf-8"))
        return parsed.get("data", {}).get("destinations", [])
    except Exception as e:
        print("ERROR: fetch_destination_locations failed -", e)


def fetch_destination_currency(amount, from_cur, to_cur):
    prompt = (
        f"You are a helpful currency converter. Convert {amount} {from_cur} to {to_cur}. "
        f"Only provide the numeric result (e.g. 123.45), with no extra text."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20,
            temperature=0
        )

        text_output = response.choices[0].message.content.strip()
        print("DEBUG: GPT Currency Conversion Response ->", text_output)

        match = re.search(r"([\d.,]+)", text_output)
        if match:
            return float(match.group(1).replace(",", "")) 
    except Exception as e:
        print("GPT Conversion error:", e)

    return None  



def process_user_request():
    user = get_user_input()
    
    print("\nFetching travel data... Please wait.\n")

    hotels = fetch_hotels(user["destination"], user["currency"])
    events = fetch_events(user["destination"], user["currency"])
    costs = get_transport_food_cost(user["destination"], user["pax"], user["days"])

    visa_info = None
    if user["visa_enabled"]:
        visa_info = get_visa_info("User_Country", user["destination"])

    total_cost = costs["total_cost"]["mid_range"]

    print("\n--- Travel Cost Breakdown ---")
    print(f"Destination: {user['destination']}")
    print(f"People: {user['pax']}")
    print(f"Days: {user['days']}")
    print(f"Budget: {user['currency']} {user['budget']}")

    print("\n--- Hotels ---")
    for hotel in hotels:
        # Note: using 'price' here might need to be replaced with one of the price keys as per your design.
        print(f"Name: {hotel.get('name', 'Unknown')}, Price: {hotel.get('price_in_user_currency', 'N/A')} {user['currency']}")

    print("\n--- Events/Places ---")
    for event in events:
        # Note: using 'price' here might need to be replaced with one of the price keys as per your design.
        print(f"Name: {event['name']}, Price: {event.get('price_in_user_currency', 'N/A')} {user['currency']}")

    print("\n--- Transport & Food Costs ---")
    print(f"Low Budget: {costs['total_cost']['low_budget']} {user['currency']}")
    print(f"Mid Budget: {costs['total_cost']['mid_range']} {user['currency']}")
    print(f"Luxury: {costs['total_cost']['luxury']} {user['currency']}")

    if visa_info:
        print("\n--- Visa Information ---")
        print(visa_info)

    print("\n--- Estimated Total Cost ---")
    print(f"{user['currency']} {total_cost}")
    return []


if __name__ == "__main__":
    process_user_request()
