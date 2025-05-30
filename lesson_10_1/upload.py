import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://the-internet.herokuapp.com/upload"

driver.get(url=url)
upload_file = driver.find_element("xpath", "//input[@type='file']")
upload_file.send_keys(f"{os.getcwd()}\downloads\learn.jpg")

time.sleep(5)