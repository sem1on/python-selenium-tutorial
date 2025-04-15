import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


serice = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=serice)

url = "https://yandex.ru/"

driver.get(url=url)
time.sleep(7)

driver.back()
time.sleep(3)
driver.forward()
driver.refresh()