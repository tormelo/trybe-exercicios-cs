import os
import requests
from parsel import Selector

my_dir = os.path.dirname(__file__)
os.mkdir(os.path.join(my_dir, "country_flags"))

BASE_URL = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"

response = requests.get(BASE_URL)
selector = Selector(response.text)
flags_url = selector.css(".gallerybox .image img::attr(src)").getall()
for img_url in flags_url:
    filename = img_url.split("/")[-1]
    image_content = requests.get("https:" + img_url).content
    file_path = os.path.join(my_dir, f"country_flags/{filename}")
    with open(file_path, "wb") as file:
        file.write(image_content)
