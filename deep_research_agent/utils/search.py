import requests
from config import ARXIV_API_URL

def search_arxiv(query, max_results=5):
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results
    }
    response = requests.get(ARXIV_API_URL, params=params)
    if response.status_code == 200:
        return response.text  # XML, can be parsed for titles/abstracts
    return ""

def search_duckduckgo(query):
    url = "https://duckduckgo.com/html/"
    params = {"q": query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text  # HTML, can be parsed for snippets
    return ""
