from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.wikipedia.org/"

driver.get(url=url) 

url_current = driver.current_url
print(f"URL запрашиваемой страницы: {url_current}.")