# Tourly - AI-Powered Travel Recommendation Website

Tourly is an AI-powered travel website built with Django. It provides personalized travel recommendations based on visa requirements and budget constraints. The platform integrates ChatGPT to dynamically generate recommendations and even build travel itineraries with detailed roadmaps including timings, costs, and activity suggestions.

**Author:** Yan

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **User Authentication & Profile Management:**  
  Users can register, log in, and update their profiles (including setting their citizenship and travel preferences).

- **Visa Recommendations:**  
  Based on the user's passport country, Tourly provides visa-related recommendations (visa-free, e-visa, visa required) for various destinations. Recommendations are color-coded (e.g., red for Visa Required, blue for E-Visa, green for No Visa Required).

- **Budget-Based Destination Suggestions:**  
  Users input their travel budget, and the system recommends destinations along with estimated travel costs and itinerary details.

- **Dynamic Itinerary Generation:**  
  The platform generates a travel roadmap/itinerary that details day-by-day activities (such as transport, attractions, dining, etc.) based on user inputs.

- **ChatGPT Integration:**  
  Tourly uses the OpenAI ChatGPT API to dynamically generate visa and budget recommendations, as well as to help create detailed itineraries.

- **Toggle Options:**  
  Users can toggle visa and budget recommendation features on or off as needed.

---

## Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Containerization:** Docker & Docker Compose
- **Frontend:** HTML, CSS (custom styling), JavaScript
- **AI Integration:** OpenAI ChatGPT API

---

## Setup Instructions

### Prerequisites

- **Docker & Docker Compose:** Ensure Docker and Docker Compose are installed on your system.
- **Git:** To clone the repository.
- **OpenAI API Key:** An API key from OpenAI for ChatGPT integration.
- **Python (3.9+):** If you plan to run the project locally outside Docker.

### Clone the Repository

```bash
git clone https://github.com/aegusten/tourly.git
cd tourly
