Your goal is to build a dynamic travel search system that provides users with relevant travel information without any hardcoded data. The system should be fully API-driven and fetch real-time data based on user input.

🔹 Main Features & Objectives
✅ 1. User Inputs
Users enter a destination (country).
Optional fields:
Pax (Number of travelers)
Days of stay
Budget (Only for logged-in users)
Currency (To show converted costs)
Visa feature toggle (Only for logged-in users with a country set)
✅ 2. Search Results (Main Output)
For the entered destination (country):

Find 3 locations within the country → State, City, or Town.
For each of the 3 locations:
2 hotels (Image, stars, price, etc.).
3 events or attractions (Image, price, details, etc.).
Average transport & food cost per pax (Fetched via GPT).
Visa requirements (Fetched via GPT if enabled).
Total estimated budget based on:
Hotel price
Event costs
Transport & food cost per person
Number of pax & days staying
Currency conversion:
Show the total cost in both the destination's currency and the user’s selected currency.
✅ 3. Result Details (Expanded View)
When a user clicks "Check", a detailed view of the location should open, showing:
Hotel details
Events details
Transport & food cost breakdown
Visa requirement (if enabled)
Converted price for user-selected currency
✅ 4. Important Functional Requirements
🚫 No Hardcoded Data → Everything must be fetched dynamically from APIs.
🔄 Results Persist → Search results should not be cleared unless the user manually refreshes or enters a new destination.
🔐 Budget & Visa Feature Restrictions:
Only logged-in users can set a budget and use the visa feature.
Visa feature is disabled if the user hasn’t set their country in the profile.
🌍 Currency Conversion → Total cost should be displayed in both local and user-preferred currency.
🔹 APIs Being Used
Feature	API Used
Fetch States, Cities, Towns	Booking.com API
Fetch Hotels	TripAdvisor API
Fetch Events & Attractions	Booking.com API
Fetch Visa Requirements	Visa API / ChatGPT
Fetch Transport & Food Cost	ChatGPT
Convert Currency	Currency Exchange API