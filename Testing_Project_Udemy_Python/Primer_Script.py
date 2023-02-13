from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path="Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

driver.maximize_window()
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fes%2F")

