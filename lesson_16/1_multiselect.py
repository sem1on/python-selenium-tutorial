import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

base_url = "https://the-internet.herokuapp.com/dropdown"

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

driver.get(base_url)

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))

DROPDOWN.select_by_visible_text("Option 1") # Выбор по тексту
DROPDOWN.select_by_value("2") # Выбор по значению
DROPDOWN.select_by_index(2)# Выбор по индексу

time.sleep(5)