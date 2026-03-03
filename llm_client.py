import os
from openai import OpenAI
import requests

PROVIDER = "OPENROUTER"

# Fetch API key from environment variable, fallback to dummy string for the repository
api_key = os.environ.get("OPENROUTER_API_KEY", "your_openrouter_api_key_here")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def get_available_models() -> list:
    try:
        req = requests.get("https://openrouter.ai/api/v1/models", headers={"Authorization": f"Bearer {client.api_key}"}, timeout=10)
        if req.status_code == 200:
            return req.json().get("data", [])
    except Exception as e:
        print(f"Error fetching models: {e}")
    return []

def generate_text(prompt: str, model_id: str = "mistralai/mistral-7b-instruct") -> str:
    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
