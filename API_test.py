import requests

url = "http://127.0.0.1:5001/predict"
data = {"features": [0.1, 1.2, 3.4, 5.6]}  # Adjust to your model's input format
response = requests.post(url, json=data)
print(response.json())