from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.wikipedia.org/"

driver.get(url=url) 

current_url = driver.current_url
current_title = driver.title
print(f"URL запрашиваемой страницы: {current_url}.")
print(f"Title запрашиваемой страницы: {current_title}.")