from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--start-maximized")
options.add_argument("--headless")

firefox = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", options=options
)


def scrape(url):
    firefox.get(url)

    paragraphs = firefox.find_elements(By.TAG_NAME, "p")

    for p in paragraphs:
        print(p.text)

    firefox.quit()


scrape(
    "https://www.wikimetal.com.br/"
    "iron-maiden-scorpions-kiss-veja-melhores-albuns-1982/"
)
