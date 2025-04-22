import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

base_url = "https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8"

driver.get(base_url)

GEOGRAPHY_LOCATOR = ("xpath", "//h3[@id='География']")
geography = driver.find_element(*GEOGRAPHY_LOCATOR)

action.scroll_to_element(geography).perform()

scrolls.scroll_to_element(geography)