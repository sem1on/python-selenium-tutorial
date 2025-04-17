import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()

chrome_options.page_load_strategy = ("normal") # ожидание полной загрузки страницы (дефолт)
chrome_options.page_load_strategy = ("eager") # ожидание толькло DOM

chrome_options.add_argument("--headless") # завпуск в фоне
chrome_options.add_argument("--incognito") # режим ингогнито
chrome_options.add_argument("--ignore-certificate-errors") # пропуск отсутствия сертификата
chrome_options.add_argument( "--disable-cache") # отключить кэш
chrome_options.add_argument("--window-size=X,Y") # размер окна

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)