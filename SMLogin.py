from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.surveymonkey.com/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"wds-button  wds-button--charcoal  wds-button--text  wds-button--sm").click()

