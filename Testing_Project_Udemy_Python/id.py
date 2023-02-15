from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_service = Service(executable_path="Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fes%2F")
time.sleep(1)

user = driver.find_element(By.NAME, 'email')
password = driver.find_element(By.NAME, 'password')
time.sleep(5)

user.send_keys("abcdefgh@gmail.com")
time.sleep(5)
password.send_keys("ghuert123456.")
time.sleep(1)
boton = driver.find_element(By.TAG_NAME, 'BUTTON')
time.sleep(5)
boton.click()

driver.quit()