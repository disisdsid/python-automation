import requests
import time

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "my-api-key"

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "gpt-3.5-turbo-16k",
    "prompt": "write python script for Hello World",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 429:
    print("Rate limit exceeded. Please check your API usage.")
    # Optionally, wait for some time before retrying
    time.sleep(60)  # Sleep for 60 seconds, adjust as needed
    # Retry the API request
    response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status_code: {response.status_code}")
    print(response.text)
