import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)

base_url = "https://the-internet.herokuapp.com/drag_and_drop"

driver.get(base_url)

COLUM_A = ("xpath", "//div[@id='column-a']")
COLUM_B = ("xpath", "//div[@id='column-b']")

A = driver.find_element(*COLUM_A)
B = driver.find_element(*COLUM_B)

action.drag_and_drop(A, B).perform()

time.sleep(3)