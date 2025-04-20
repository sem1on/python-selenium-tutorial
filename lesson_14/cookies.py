import time
import pickle
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/ru")

singl_cookie = driver.get_cookie("country_code") # Получение одной cookie
all_cookies = driver.get_cookies() # Получение всех cookies

add_cookie = driver.add_cookie({ # Добавление своих cookies
    "name": "My_cookie",
    "value": "21"
})
my_cookie = driver.get_cookie("My_cookie")

driver.delete_cookie("split") # Замена cookie через удаление и добавление
after = driver.add_cookie({
    "name": "split",
    "value": "new_value"
})

pickle.dump(driver.get_cookies(), open(os.getcwd()+"/lesson_14/cookies/cookies.pkl", "wb")) #


driver.delete_all_cookies() #Очистка старых cookies
cookies = pickle.load(open(os.getcwd()+"/lesson_14/cookies/cookies.pkl", "rb")) # Добавление новых из файла cookies
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh() # Перезагрузка страницы

