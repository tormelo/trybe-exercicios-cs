from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--start-maximized")

firefox = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", options=options
)


def scrape(url):
    firefox.get(url)

    quote = firefox.find_element(By.CLASS_NAME, "text").get_attribute(
        "innerHTML"
    )

    print(quote)

    firefox.quit()


scrape("https://quotes.toscrape.com/")
