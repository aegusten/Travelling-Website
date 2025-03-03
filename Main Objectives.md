Main Objectives
User Registration and Profile Customization:

Allow travelers to register and update their profiles.
Let users specify their passport country (citizenship) and travel preferences (like travel style and dietary needs).
Visa Recommendations:

Objective: Use AI (ChatGPT API) or pre-seeded data to suggest destination countries based on the user’s passport country.
Design:
Display a catalog of countries with visa information.
Color-code the visa types:
Red: Visa Required
Blue: E-Visa Available
Green: No Visa Required
Include additional details like the number of visa-free days if applicable.
Conditional Display: If the user hasn’t set their passport country, do not show these recommendations.
Budget-Based Recommendations and Itinerary Planning:

Objective: Let users input their travel budget and then recommend destinations, attractions, hotels, restaurants, and entertainment options that fit within that budget.
Design:
Use AI (ChatGPT API, plus external travel APIs later) to generate detailed itinerary suggestions.
Present a dynamic “roadmap” or timeline that outlines:
Time-based itinerary steps: For example, departure time, estimated transit (e.g., taxi fare and travel time to the hotel), and subsequent activities (with images, ratings, cost estimates, and duration).
Include a toggle to switch between visa and budget recommendations.
Dynamic User Interface with Toggles:

Objective: Enable users to switch the display of visa recommendations and budget recommendations on or off.
Design:
Two toggle buttons on the dashboard allow users to control which recommendations (visa, budget, or both) are displayed.
Results update dynamically (using AJAX or similar techniques) without a full page reload.
Future AI Integration:

Objective: Use AI to generate personalized travel suggestions that integrate both visa rules and budget constraints.
Design:
Build functions that send prompts to ChatGPT to fetch structured JSON data with recommendations.
Combine this AI-generated data with data from external travel APIs to offer a comprehensive itinerary.
Design Overview
Dashboard Layout:
The dashboard (using the Tourly template) displays a header with login/profile options. Once logged in and with a passport country set, the user sees a catalog of destination recommendations that include visa and budget information.

Color-Coding & Visual Timeline:
Visa requirements are shown in color (red, blue, green) and the itinerary is visually represented as a timeline (with boxes representing itinerary items, connected by lines indicating transit times and costs).

Dynamic Interactions:
Frontend toggles (for visa and budget) and input fields (like destination and budget) allow users to refine their recommendations dynamically.

Backend Integration:
The backend uses Django models to store core data (users, countries, visa rules, itineraries, etc.) and incorporates ChatGPT API calls to generate dynamic suggestions based on user inputs.

