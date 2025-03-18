import openai

# Replace with your API key
API_KEY = "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"

def test_openai_api():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello, GPT!"}],
            api_key=API_KEY  # Pass the API key explicitly
        )
        print("API Key is working! Response:")
        print(response["choices"][0]["message"]["content"])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_openai_api()
