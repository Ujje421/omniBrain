import requests

def research(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    data = requests.get(url).json()
    return data.get("Abstract", "No result found")
