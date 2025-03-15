import http.client
import json
import openai

RAPIDAPI_KEY = "011df194f4msh1c49b868985b11bp109a8djsn15935cbecfea"
openai.api_key = "YOUR_OPENAI_KEY"

def get_visa_requirement(passport="US", destination="BH"):
    conn = http.client.HTTPSConnection("visa-requirement.p.rapidapi.com")
    payload = f"passport={passport}&destination={destination}"
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "visa-requirement.p.rapidapi.com",
        'Content-Type': "application/x-www-form-urlencoded"
    }
    print("DEBUG: Calling get_visa_requirement with payload:", payload)
    conn.request("POST", "/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    try:
        parsed = json.loads(data.decode("utf-8"))
        print("DEBUG: get_visa_requirement response:", parsed)
        return parsed
    except Exception as e:
        print("DEBUG: get_visa_requirement parse error:", e)
        return data.decode("utf-8")

def convert_currency_http(from_cur="USD", to_cur="EUR,GBP"):
    conn = http.client.HTTPSConnection("currency-conversion-and-exchange-rates.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }
    url = f"/latest?from={from_cur}&to={to_cur}"
    print("DEBUG: Calling convert_currency_http with URL:", url)
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    try:
        parsed = json.loads(data.decode("utf-8"))
        print("DEBUG: convert_currency_http response:", parsed)
        return parsed
    except Exception as e:
        print("DEBUG: convert_currency_http parse error:", e)
        return data.decode("utf-8")

def fetch_airbnb_properties(location="london", currency="USD", adults=1, totalRecords=10):
    conn = http.client.HTTPSConnection("airbnb19.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "airbnb19.p.rapidapi.com"
    }
    url = f"/api/v1/searchPropertyByLocationV2?location={location}&totalRecords={totalRecords}&currency={currency}&adults={adults}"
    print("DEBUG: Calling fetch_airbnb_properties with URL:", url)
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    try:
        parsed = json.loads(data.decode("utf-8"))
        print("DEBUG: fetch_airbnb_properties response:", parsed)
        return parsed
    except Exception as e:
        print("DEBUG: fetch_airbnb_properties parse error:", e)
        return data.decode("utf-8")

def fetch_booking_reviews(attraction_id="PR6K7ZswbGBs", page=1):
    conn = http.client.HTTPSConnection("booking-com15.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': "booking-com15.p.rapidapi.com"
    }
    url = f"/api/v1/attraction/getAttractionReviews?id={attraction_id}&page={page}"
    print("DEBUG: Calling fetch_booking_reviews with URL:", url)
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    try:
        parsed = json.loads(data.decode("utf-8"))
        print("DEBUG: fetch_booking_reviews response:", parsed)
        return parsed
    except Exception as e:
        print("DEBUG: fetch_booking_reviews parse error:", e)
        return data.decode("utf-8")
    
def get_budget_recommendations(budget, additional_context=""):
    prompt = (
        f"You are a helpful travel assistant. A traveler has a budget of ${budget}.\n"
        f"Given that they're looking at: {additional_context}, suggest 2 other countries under this budget.\n"
        "Return them as valid JSON with keys: 'destination', 'estimated_cost', 'description', and 'image_url'."
    )

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.4,
        max_tokens=600,
    )

    try:
        raw_text = response["choices"][0]["message"]["content"]
        data = json.loads(raw_text)
        return data
    except Exception as e:
        print("GPT parse error:", e)
        return []