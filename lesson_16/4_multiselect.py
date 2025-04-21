import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

base_url = "https://demoqa.com/select-menu"

SELECT_LOCATOR = ("xpath", "input[@id='react-select-4-input']")

driver.get(base_url)

driver.find_element(*SELECT_LOCATOR).send_keys("Gr")
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.TAB)