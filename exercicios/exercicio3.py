import requests


HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
        "Safari/537.36"
    ),
    "Accept": "text/html",
}

response = requests.get(
    "https://scrapethissite.com/pages/advanced/?gotcha=headers",
    headers=HEADERS,
)

assert "Accept value is missing 'text/html'" not in response.text
assert (
    "User-Agent value doesn't look like a standard mozilla/chrome/safari value"
    not in response.text
)
