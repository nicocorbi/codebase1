import requests
import os
import dotenv
dotenv.load_dotenv()

KEY = os.getenv("KEY")
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": f"Bearer {KEY}"}
payload = {
    "inputs": "Hola mundo",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json())