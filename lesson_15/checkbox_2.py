from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

base_url = "https://demoqa.com/selectable"
driver.get(base_url)

ELEMENT_1 = ("xpath", "//li[text()='Cras justo odio']")

before = driver.find_element(*ELEMENT_1).get_attribute("class")
print(before)
driver.find_element(*ELEMENT_1).click()
after = driver.find_element(*ELEMENT_1).get_attribute("class")
assert "active" in after