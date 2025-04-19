from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servise = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=servise)
driver.implicitly_wait(10)

base_url = "https://demoqa.com/dynamic-properties"
driver.get(url=base_url)

VISIBLE_BUTTON_AFTER = ("xpath", "//button[@id='visibleAfter']")

visible_button = driver.find_element(*VISIBLE_BUTTON_AFTER)
visible_button.click()