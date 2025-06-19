import requests
from bs4 import BeautifulSoup

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("h3")
    return [r.get_text() for r in results[:5]]  # Top 5 headings
