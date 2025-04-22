import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)

base_url = "https://tympanus.net/Development/DragDropInteractions/sidebar.html"

driver.get(base_url)

GRID_ITEM = ("xpath", "//div[@class='grid__item'][4]")
SIDEBAR_ITEM = ("xpath", "//div[@class='drop-area__item'][2]")

first_box = driver.find_element(*GRID_ITEM)
second_box = driver.find_element(*SIDEBAR_ITEM)

action.click_and_hold(first_box)\
    .pause(2)\
    .move_to_element(second_box)\
    .pause(2)\
    .release()\
    .perform()

time.sleep(3)