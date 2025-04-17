import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.freeconferencecall.com/ru/ru/login"
driver.get(url=url)

login_button = driver.find_element("xpath", "//a[@id='login-desktop']")
login_button.click()

email_input = driver.find_element("xpath", "//input[@id='login_email']")
email_input.clear()
email_input.send_keys("example@mail.com")
print(email_input.get_attribute("value"))

time.sleep(5)