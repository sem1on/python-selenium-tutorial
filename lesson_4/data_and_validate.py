from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.wikipedia.org/"
driver.get(url=url) 

current_url = driver.current_url
print(f"URL запрашиваемой страницы: {current_url}.")
assert current_url == url, "Открыта не та страница, ошибка в URL"

current_title = driver.title
print(f"Title запрашиваемой страницы: {current_title}.")
assert current_title == "Wikipedia", "Title страницы не совпадает"

print(driver.page_source)