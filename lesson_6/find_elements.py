import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://demoqa.com/automation-practice-form"
driver.get(url=url)

bar_list = driver.find_elements("class name", "element-group")
bar_list[0].click

time.sleep(10)