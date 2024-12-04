import requests

API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": "Bearer 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"}


def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()


output = query({
    "inputs": "I like you. I love you",
})
emociones = output[0]
for emocion in emociones:
  print(emocion['label'] + ":", emocion['score'])
  print(emocion.get('label') + ":", emocion.get('score'))