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

    posts = []
    for post in firefox.find_elements(By.CLASS_NAME, "inhype-post"):
        new_item = dict()
        new_item["title"] = (
            post.find_element(By.CLASS_NAME, "entry-title")
            .find_element(By.TAG_NAME, "a")
            .get_attribute("innerHTML")
        )
        new_item["link"] = (
            post.find_element(By.CLASS_NAME, "entry-title")
            .find_element(By.TAG_NAME, "a")
            .get_attribute("href")
        )
        new_item["date"] = post.find_element(
            By.CLASS_NAME, "entry-date"
        ).get_attribute("innerHTML")
        posts.append(new_item)

    firefox.quit()

    return posts


print(scrape("https://diolinux.com.br/"))
