import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

base_url = "https://the-internet.herokuapp.com/key_presses"

KEYBOARD_INPUT = ("xpath", "//input[@id='target']")

driver.get(base_url)

driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.ENTER)