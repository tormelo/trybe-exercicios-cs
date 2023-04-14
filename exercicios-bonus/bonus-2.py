import requests


has_next = True
page = 1
while has_next:
    response = requests.get(
        f"http://quotes.toscrape.com/api/quotes?page={page}"
    )
    json_content = response.json()
    for quote in json_content["quotes"]:
        print(quote["text"])
    has_next = json_content["has_next"]
    page = json_content["page"] + 1
