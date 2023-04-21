
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/geckodriver-v0.33.0-win-aarch64/geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://www.surveymonkey.com/")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)

driver.get("https://www.google.com/")
driver.back()
driver.refresh()
driver.forward()


driver.close()
