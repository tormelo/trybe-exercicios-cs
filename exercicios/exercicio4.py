import requests
from bs4 import BeautifulSoup

BASE_URL = "https://pt.wikipedia.org"

page = requests.get(f"{BASE_URL}/wiki/Rock_in_Rio")
html_content = page.text
soup = BeautifulSoup(html_content, "html.parser")


def create_url_from_urn(urn: str) -> str:
    urn = urn[1:] if urn[0] == "/" else urn
    return f"{BASE_URL}/{urn}"


def get_wiki_link(link: str) -> str:
    return link if link[:4] == "http" else create_url_from_urn(link)


links = [
    get_wiki_link(anchor["href"])
    for anchor in soup.findAll("a")
    if anchor.get("href") is not None
]

for link in links:
    print(link)
