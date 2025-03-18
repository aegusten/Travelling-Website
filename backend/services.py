import http.client
import json
import openai
import urllib.parse

RAPIDAPI_KEY = "011df194f4msh1c49b868985b11bp109a8djsn15935cbecfea"
openai.api_key = "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"


# OTHER API #
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
        parsed = json.loads(data.decode("utf-8"))
        return parsed.get("result", amount)
    except:
        return amount

def fetch_airbnb_properties(location, currency, adults, totalRecords=10):
    conn = http.client.HTTPSConnection("airbnb19.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "airbnb19.p.rapidapi.com"
    }
    url = f"/api/v1/searchPropertyByLocationV2?location={location}&totalRecords={totalRecords}&currency={currency}&adults={adults}"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    try:
        return json.loads(data.decode("utf-8"))
    except:
        return None

def get_hotels(destination, currency, limit=2):
    conn = http.client.HTTPSConnection("airbnb19.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "airbnb19.p.rapidapi.com"
    }
    encoded_destination = urllib.parse.quote(destination)
    url = f"/api/v1/searchPropertyByLocationV2?location={encoded_destination}&totalRecords={limit}&currency={currency}&adults=1"
    
    print(f"DEBUG: Fetching hotels for {destination} in currency {currency}")

    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    try:
        return json.loads(data.decode("utf-8"))
    except:
        return None

def get_events(destination, limit=3):
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
        parsed = json.loads(data.decode("utf-8"))
        attractions = parsed.get("data", {}).get("products", [])
        
        events_list = []
        for attraction in attractions[:limit]:
            events_list.append({
                "name": attraction.get("name", "Unknown Event"),
                "description": attraction.get("shortDescription", ""),
                "image": attraction.get("primaryPhoto", {}).get("url", "/static/images/default.jpg"),
                "price": attraction.get("representativePrice", {}).get("amount", "N/A"),
                "currency": attraction.get("representativePrice", {}).get("currencyCode", "USD"),
            })
        
        return events_list
    except Exception as e:
        print(f"DEBUG: get_events error => {e}")
        return []

  
def calculate_total_cost(hotels, events, transport, food, days, pax):
    total_hotels = 0
    if hotels and isinstance(hotels, dict):
        hotel_list = hotels.get("data", {}).get("list", [])
        for hotel in hotel_list:
            pricing = hotel.get("pricingQuote", {}).get("structuredStayDisplayPrice", {}).get("primaryLine", {})
            price_str = pricing.get("price", "0").replace("$", "").replace(",", "")
            try:
                price = float(price_str)
            except:
                price = 0
            total_hotels += price * days * pax

    total_events = 0
    if events and isinstance(events, list):
        for event in events:
            try:
                event_cost = float(event.get("estimated_cost", 0))
            except:
                event_cost = 0
            total_events += event_cost * pax

    full_total = total_hotels + total_events + transport + food
    return full_total


def get_popular_destinations(country_name):
    conn = http.client.HTTPSConnection("tripadvisor16.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "tripadvisor16.p.rapidapi.com"
    }
    url = f"/api/v1/hotels/searchLocation?query={country_name}&languagecode=en-us"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    try:
        return json.loads(data.decode("utf-8")).get("data", [])
    except:
        return []

def fetch_destination_locations(destination):
    conn = http.client.HTTPSConnection("booking-com15.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "booking-com15.p.rapidapi.com"
    }
    
    url = f"/api/v1/attraction/searchLocation?query={destination}&languagecode=en-us"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    
    try:
        parsed = json.loads(data.decode("utf-8"))
        return parsed.get("data", {}).get("destinations", [])
    except:
        return []

# OpenAI GPT-3 API #
def get_visa_requirement_from_chatgpt(passport_country_name, destination_country_name):
    prompt = f"I am a traveler from {passport_country_name} planning to visit {destination_country_name}. What are the visa requirements?"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    visa_info = response["choices"][0]["message"]["content"].strip()
    return visa_info

def get_transport_food_cost(city, pax, days):
    prompt = f"Estimate the average transport and food cost per person per day in {city}."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert in travel cost estimation."},
                  {"role": "user", "content": prompt}]
    )

    cost_info = response.choices[0].message.content.strip()

    try:
        transport_cost, food_cost = [float(x) for x in cost_info.split(",")]
    except:
        transport_cost, food_cost = 50, 30 

    return {"transport": transport_cost * pax * days, "food": food_cost * pax * days}

