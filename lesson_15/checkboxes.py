from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

base_url = "https://demoqa.com/checkbox"

driver.get(base_url)

CHECKBOX_CLICK = ("xpath", "//span[@class='rct-checkbox']")
CHECKBOX_STATUS = ("xpath", "//input[@id='tree-node-home']")

click_check = driver.find_element(*CHECKBOX_CLICK).click()
status_check = driver.find_element(*CHECKBOX_STATUS).is_selected
assert status_check is True