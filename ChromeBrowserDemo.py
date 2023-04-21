
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
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
