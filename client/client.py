import requests

try:
    response = requests.get("http://server-container:8080")
    print(f"Response from server: {response.text}")
except requests.ConnectionError:
    print("Failed to connect to the server.")
