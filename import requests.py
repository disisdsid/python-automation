import requests

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "my-api-key"

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "gpt-4-0125-preview",
    "prompt": "write python script for Hello World",
    "max_tokens": 100,  # Corrected parameter name
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status_code: {response.status_code}")
    print(response.text)  # Print the response content for more details

