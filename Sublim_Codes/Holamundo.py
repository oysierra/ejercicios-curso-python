from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Omar SE\Downloads\Borrar\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fes%2F")

driver.close()