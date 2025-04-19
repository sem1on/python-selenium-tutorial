import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

base_url = "https://demoqa.com/alerts"

driver.get(base_url)

OPEN_ALERT_1 = ("xpath", "//button[@id='alertButton']")
OPEN_ALERT_2 = ("xpath", "//button[@id='confirmButton']")

# Принять алерт с одной кнопкой
open_alert = wait.until(EC.element_to_be_clickable(OPEN_ALERT_1))
open_alert.click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.accept()
time.sleep(3)

# Отклонить алерт
open_alert = wait.until(EC.element_to_be_clickable(OPEN_ALERT_2))
open_alert.click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.send_keys("Hello!") #Ввод текста в алерт
print(alert.text) # Получение текста из алерта
alert.dismiss()
time.sleep(3)

