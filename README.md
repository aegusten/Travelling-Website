# Tourly - AI-Powered Travel Recommendation Website

Tourly is an AI-powered travel website built with Django. It provides **personalized travel recommendations** based on **visa requirements** and **budget constraints**. The platform integrates **ChatGPT** to dynamically generate travel suggestions and build **detailed itineraries**, including **timings, costs, and activity recommendations**.

**Author:** Yan

---

## 📖 **Table of Contents**
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 **Features**
- **🔑 User Authentication & Profile Management**  
  Users can register, log in, and update their profiles, including setting their **citizenship** and **travel preferences**.

- **🛂 Visa-Based Travel Recommendations**  
  Tourly provides **color-coded visa recommendations** based on the user's passport country:  
  - 🟢 **No Visa Required**  
  - 🔵 **E-Visa Available**  
  - 🔴 **Visa Required**  

- **💰 Budget-Based Destination Suggestions**  
  Users enter their **travel budget**, and the system recommends destinations with estimated costs and itinerary details.

- **📍 AI-Powered Itinerary Generator**  
  Tourly creates a **day-by-day itinerary**, detailing activities such as **transport, attractions, dining, and more**.

- **🤖 ChatGPT Integration**  
  The OpenAI ChatGPT API helps generate **visa and budget recommendations** and assists in creating **custom itineraries**.

- **⚙️ Toggle Options**  
  Users can **enable/disable visa and budget recommendations** as per their needs.

---

## 🛠️ **Tech Stack**
- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Containerization:** Docker & Docker Compose
- **Frontend:** HTML, CSS, JavaScript
- **AI Integration:** OpenAI ChatGPT API

---

## 🔧 **Setup Instructions**

### **Prerequisites**
Before you begin, ensure you have the following installed:
- **Docker & Docker Compose** (for containerized setup)
- **Git** (to clone the repository)
- **Python (3.9+)** (if running the project locally without Docker)
- **OpenAI API Key** (for ChatGPT integration)

### **Clone the Repository**
```bash
git clone https://github.com/aegusten/tourly.git
cd tourly
