import requests

def fetch_api_placeholder():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
    response.raise_for_status()
    return response.json()