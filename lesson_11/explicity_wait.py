from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

base_url = "https://demoqa.com/dynamic-properties"
second_url = "https://the-internet.herokuapp.com/dynamic_controls"
driver.get(base_url)
driver.get(second_url)

VISIBLE_BUTTON_AFTER = ("xpath", "//button[@id='visibleAfter']")
ENABLE_AFTER_BUTTON = ("xpath", "//button[@id='enableAfter']")
REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
EN_DIS_BUTTON = ("xpath", "//button[text()='Enable']")
DISABLE_INPUT = ("xpath", "//input[@type='text']")

visible_button = wait.until(EC.visibility_of_element_located(VISIBLE_BUTTON_AFTER))
visible_button.click()

enabel_button = wait.until(EC.element_to_be_clickable(ENABLE_AFTER_BUTTON))
enabel_button.click()

driver.find_element(*REMOVE_BUTTON)
remove_button = wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
print("OK!")

en_dis_batton = wait.until(EC.element_to_be_clickable(EN_DIS_BUTTON)).click()
enable_input = wait.until(EC.element_to_be_clickable(DISABLE_INPUT)).send_keys("Hello!")
check_text = wait.until(EC.text_to_be_present_in_element_value(DISABLE_INPUT, enable_input))
print("OK!")