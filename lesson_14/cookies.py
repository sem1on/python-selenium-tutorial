import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/ru")

singl_cookie = driver.get_cookie("country_code") # Получение одной cookie
all_cookies = driver.get_cookies() # Получение всех cookies

add_cookie = driver.add_cookie({ # Добавление своих cookies
    "name": "My_cookie",
    "value": "21"
})

my_cookie = driver.get_cookie("My_cookie")
print(my_cookie)