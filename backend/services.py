import os
import json
import openai
import requests
import urllib.parse
import http.client

RAPIDAPI_KEY = "011df194f4msh1c49b868985b11bp109a8djsn15935cbecfea"
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
    conn = http.client.HTTPSConnection("currency-conversion-and-exchange-rates.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }
    url = f"/convert?from={from_cur}&to={to_cur}&amount={amount}"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    try:
        return json.loads(data.decode("utf-8")).get("result", amount)
    except:
        return amount


def fetch_hotels(destination, user_currency, limit=2):
    conn = http.client.HTTPSConnection("airbnb19.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "airbnb19.p.rapidapi.com"
    }
    encoded_destination = urllib.parse.quote(destination)
    url = f"/api/v1/searchPropertyByLocationV2?location={encoded_destination}&totalRecords={limit}&currency=USD&adults=1"

    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    try:
        hotel_list = json.loads(data.decode("utf-8"))["data"]["list"]
        converted_hotels = []
        
        for hotel in hotel_list:
            hotel_price = hotel.get("price", 0)
            hotel_currency = hotel.get("currency", "USD")

            destination_currency = fetch_destination_currency(destination)
            hotel_price_in_destination_currency = convert_currency(hotel_price, from_cur=hotel_currency, to_cur=destination_currency)
            hotel_price_in_user_currency = convert_currency(hotel_price_in_destination_currency, from_cur=destination_currency, to_cur=user_currency)

            converted_hotels.append({
                "name": hotel.get("name", "Unknown"),
                "description": hotel.get("description", ""),
                "image_url": hotel.get("image_url", fetch_image(destination)),
                "price_in_destination_currency": hotel_price_in_destination_currency,
                "destination_currency": destination_currency,
                "price_in_user_currency": hotel_price_in_user_currency,
                "user_currency": user_currency,
                "rating": hotel.get("rating", "N/A"),
                "amenities": hotel.get("amenities", "N/A"),
            })
        
        return converted_hotels
    except:
        return []


def fetch_events(destination, user_currency, limit=3):
    conn = http.client.HTTPSConnection("booking-com15.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "booking-com15.p.rapidapi.com"
    }
    
    encoded_destination = urllib.parse.quote(destination)
    url = f"/api/v1/attraction/searchAttractions?id={encoded_destination}&sortBy=trending&page=1&languagecode=en-us"
    
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    
    try:
        attractions = json.loads(data.decode("utf-8")).get("data", {}).get("products", [])
        destination_currency = fetch_destination_currency(destination)

        converted_events = []
        for event in attractions[:limit]:
            event_price = event.get("representativePrice", {}).get("amount", 0)
            event_original_currency = event.get("representativePrice", {}).get("currencyCode", "USD")

            event_price_in_destination_currency = convert_currency(event_price, from_cur=event_original_currency, to_cur=destination_currency)
            event_price_in_user_currency = convert_currency(event_price_in_destination_currency, from_cur=destination_currency, to_cur=user_currency)

            converted_events.append({
                "name": event.get("name", "Unknown Event"),
                "description": event.get("shortDescription", ""),
                "image_url": event.get("primaryPhoto", {}).get("url", fetch_image(destination)),
                "price_in_destination_currency": event_price_in_destination_currency,
                "destination_currency": destination_currency,
                "price_in_user_currency": event_price_in_user_currency,
                "user_currency": user_currency
            })
        
        return converted_events
    except:
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

    try:
        transport_data, food_data = cost_info.split(" | ")
        transport_low, transport_mid, transport_high = [float(x) for x in transport_data.split(": ")[1].split(",")]
        food_low, food_mid, food_high = [float(x) for x in food_data.split(": ")[1].split(",")]
    except:
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
        if "urls" in data:
            return data["urls"]["regular"]
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

    try:
        parsed = json.loads(data.decode("utf-8"))
        return parsed.get("data", {}).get("destinations", [])
    except Exception as e:
        print(f"ERROR: fetch_destination_locations failed - {e}")


def fetch_destination_currency(destination):
    conn = http.client.HTTPSConnection("currency-conversion-and-exchange-rates.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }
    url = f"/currency?country={urllib.parse.quote(destination)}"

    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    try:
        parsed = json.loads(data.decode("utf-8"))
        return parsed.get("currencyCode", "USD")
    except Exception as e:
        print(f"ERROR: fetch_destination_currency failed - {e}")
        return "USD" 
     

def process_user_request():
    user = get_user_input()
    
    print("\nFetching travel data... Please wait.\n")

    hotels = fetch_hotels(user["destination"], user["currency"])
    events = fetch_events(user["destination"])
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
        print(f"Name: {hotel.get('name', 'Unknown')}, Price: {hotel.get('price', 'N/A')} {user['currency']}")

    print("\n--- Events/Places ---")
    for event in events:
        print(f"Name: {event['name']}, Price: {event['price']} {event['currency']}")

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
