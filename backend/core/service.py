import openai
import json

openai.api_key = 'API_KEY'

def get_visa_recommendations(passport_country):
    prompt = (
        f"Provide a list of travel destinations for a citizen of {passport_country} "
        "with the visa requirement categories (No Visa, E-Visa, Visa Required) and the allowed number of visa-free days if applicable. "
        "Return the result as a JSON array with objects that have keys: 'destination', 'visa_requirement', and 'visa_free_days' (if applicable)."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500,
    )
    
    try:
        data = json.loads(response.choices[0].message.content)
    except Exception as e:
        data = {"error": f"Parsing error: {e}"}
    return data

def get_budget_recommendations(budget, additional_context=""):
    prompt = (
        f"For a traveler with a budget of ${budget}, provide a list of recommended travel destinations along with "
        "estimated travel costs and visa requirements. If available, include information like visa-free days or e-visa duration. "
        f"{additional_context} Return the results as a JSON array with keys: 'destination', 'estimated_cost', and 'visa_requirement'."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=500,
    )
    
    try:
        data = json.loads(response.choices[0].message.content)
    except Exception as e:
        data = {"error": f"Parsing error: {e}"}
    return data
