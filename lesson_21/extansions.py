import time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_extension("D:\IT\PythonSelenium\lesson_21\extensions\adblock.crx")

driver = webdriver.Chrome(options=options)
driver.get("https://ya.ru")

time.sleep(5)
