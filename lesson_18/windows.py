from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

base_url = "https://hyperskill.org/"

LOCATOR_1 = ("xpath", "//a[text()='For Business']")
BUTTON_LOCATOR = ("xpath", "//a[text()='Start for Free']")

driver.find_element(*LOCATOR_1).click()
tabs = driver.window_handles
driver.switch_to(tabs[1])
driver.find_element(*BUTTON_LOCATOR).click()