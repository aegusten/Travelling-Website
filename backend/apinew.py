import requests
import os
RAPIDAPI_KEY = "de188ee5a7mshed60a3dc2f98e64p16b427jsn29ca586b8f21"
# API Hosts
BOOKING_HOST = "booking-com15.p.rapidapi.com"
AIRBNB_HOST = "airbnb19.p.rapidapi.com"
CURRENCY_HOST = "currency-conversion-and-exchange-rates.p.rapidapi.com"
VISA_HOST = "visa-requirement.p.rapidapi.com"
GOOGLE_MAPS_HOST = "google-map-places.p.rapidapi.com"

# Test Parameters
DESTINATION = "New York, USA"
CURRENCY = "USD"
ADULTS = 2
HOTEL_RECORDS = 5
AMOUNT_TO_CONVERT = 100
FROM_CURRENCY = "USD"
TO_CURRENCY = "EUR"
PASSPORT_COUNTRY = "US"
DESTINATION_COUNTRY = "BH"
ATTRACTION_ID = "PR6K7ZswbGB"  # Example Attraction ID

# 🔍 Check if API Key is set
if not RAPIDAPI_KEY:
    raise ValueError("❌ API Key is missing! Please set RAPIDAPI_KEY.")

# 1️⃣ Booking.com API (Get Attraction Reviews)
def get_attraction_reviews(attraction_id):
    print("\n🌍 Testing Booking.com API (Get Attraction Reviews)...")
    url = f"https://{BOOKING_HOST}/api/v1/attraction/getAttractionReviews"
    params = {"id": attraction_id, "page": 1}
    headers = {"x-rapidapi-key": RAPIDAPI_KEY, "x-rapidapi-host": BOOKING_HOST}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 401:
        print("❌ Unauthorized - Check API Key!")
        return
    elif response.status_code != 200:
        print(f"❌ API Error {response.status_code}: {response.text}")
        return

    data = response.json()
    print(f"✅ Attraction Reviews: {data}")

# 2️⃣ Airbnb Property Search API
def fetch_hotels_airbnb(lat, lng, currency, adults=1, records=10):
    print("\n🏨 Testing Airbnb API...")
    url = f"https://{AIRBNB_HOST}/api/v1/searchPropertyByLocationV2"
    params = {"location": f"{lat},{lng}", "totalRecords": records, "currency": currency, "adults": adults}
    headers = {"x-rapidapi-key": RAPIDAPI_KEY, "x-rapidapi-host": AIRBNB_HOST}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 401:
        print("❌ Unauthorized - Check API Key!")
        return
    elif response.status_code != 200:
        print(f"❌ API Error {response.status_code}: {response.text}")
        return

    data = response.json()
    results = []
    for item in data.get("data", []):
        results.append({
            "name": item.get("title", "No Title"),
            "price": item.get("price", 0),
            "rating": item.get("rating", 0),
            "image_url": item.get("images", [])[0] if item.get("images") else None
        })

    if results:
        print(f"✅ Found {len(results)} properties near {DESTINATION}:")
        for hotel in results:
            print(f"   - {hotel['name']} | Price: {hotel['price']} {CURRENCY} | Rating: {hotel['rating']}")
    else:
        print("❌ No properties found.")

# 3️⃣ Currency Conversion API
def convert_currency(amount, from_cur, to_cur):
    print("\n💰 Testing Currency Conversion API...")
    if from_cur == to_cur:
        print(f"✅ No conversion needed: {amount} {from_cur}")
        return amount

    url = f"https://{CURRENCY_HOST}/latest"
    params = {"from": from_cur, "to": to_cur}
    headers = {"x-rapidapi-key": RAPIDAPI_KEY, "x-rapidapi-host": CURRENCY_HOST}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 401:
        print("❌ Unauthorized - Check API Key!")
        return amount
    elif response.status_code != 200:
        print(f"❌ API Error {response.status_code}: {response.text}")
        return amount

    data = response.json()
    if "rates" in data and to_cur in data["rates"]:
        rate = data["rates"][to_cur]
        converted = amount * rate
        print(f"✅ {amount} {from_cur} -> {converted:.2f} {to_cur}")
        return converted
    else:
        print("❌ Currency conversion failed.")
        return amount

# 4️⃣ Visa Requirement API
def check_visa_requirement(passport, destination):
    print("\n🛂 Testing Visa Requirement API...")
    url = f"https://{VISA_HOST}/"
    payload = f"passport={passport}&destination={destination}"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": VISA_HOST,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 401:
        print("❌ Unauthorized - Check API Key!")
        return
    elif response.status_code != 200:
        print(f"❌ API Error {response.status_code}: {response.text}")
        return

    data = response.json()
    print(f"✅ Visa requirement for {passport} to {destination}: {data}")

# ✅ Run all tests
if __name__ == "__main__":
    # Test API Key
    print(f"🔑 Testing with API Key: {RAPIDAPI_KEY[:5]}****")

    # Test Booking.com API
    get_attraction_reviews(ATTRACTION_ID)

    # Test Geocode API
    lat, lng = geocode_destination(DESTINATION)
    if lat and lng:
        fetch_hotels_airbnb(lat, lng, CURRENCY, ADULTS, HOTEL_RECORDS)

    # Test Currency Conversion
    convert_currency(AMOUNT_TO_CONVERT, FROM_CURRENCY, TO_CURRENCY)

    # Test Visa Requirement API
    check_visa_requirement(PASSPORT_COUNTRY, DESTINATION_COUNTRY)