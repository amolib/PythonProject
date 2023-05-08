from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

name = "Amol"
service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert= driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept() #it will click on the OK button which will be there on popup window
#alert.dismiss() #it will click on the Cancel button which will be there on popup window

