import requests

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.content
image_bytes = query({
  "inputs": "Astronaut riding a horse",
})

import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.save("plane.png")