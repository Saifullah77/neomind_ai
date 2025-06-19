import requests
from bs4 import BeautifulSoup

def read_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()
