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

all_options = DROPDOWN.options

for option in all_options:
    DROPDOWN.select_by_visible_text(option.text)
    if "Option 1" in option.text:
        print("Опция присутствует")

for option in all_options:
    DROPDOWN.select_by_index(all_options.index(option))

for option in all_options:
    DROPDOWN.select_by_value(option.get_attribute("value"))

