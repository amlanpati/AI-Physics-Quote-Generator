import requests
import os
from dotenv import load_dotenv
load_dotenv()

apiKey = os.getenv("API_KEY")

def get_physics_quote(topic):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={apiKey}"

    payload = {
        "contents": [{
            "parts": [{"text": f"Give me a short, inspiring physics quote about {topic}."}]
        }]
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        quote = data['candidates'][0]['content']['parts'][0]['text']
        print(f"\nAI Physics Quote:\n{quote}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    topic = input("Enter a physics topic (e.g. gravity, time, entropy):")
    get_physics_quote(topic)