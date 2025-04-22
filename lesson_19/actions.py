import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)

base_url = "https://testkru.com/Elements/Buttons"

driver.get(base_url)

LEFT_CLICK_BUTTON = ("xpath", "//button[@id='leftClick']")
RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClick']")
DUBL_CLICK_BUTTON = ("xpath", "//button[@id='doubleClick']")
HOVER_BUTTON = ("xpath", "//button[@id='colorChangeOnHover']")

left_click = driver.find_element(*LEFT_CLICK_BUTTON)
right_click = driver.find_element(*RIGHT_CLICK_BUTTON)
dubl_click = driver.find_element(*DUBL_CLICK_BUTTON)
hover_button = driver.find_element(*HOVER_BUTTON)



action.click(left_click).perform()
action.context_click(right_click).perform()
action.double_click(dubl_click).perform()
action.move_to_element(hover_button).perform()

action.click(left_click)\
    .pause(1)\
    .context_click(right_click)\
    .pause(1)\
    .double_click(dubl_click)\
    .pause(1)\
    .move_to_element(hover_button)\
    .pause(1)\
    .perform()

time.sleep(3)
