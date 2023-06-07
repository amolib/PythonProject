from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")