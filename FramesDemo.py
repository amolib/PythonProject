from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://selectorshub.com/xpath-practice-page/")
driver.find_element(By.ID,"userId").send_keys("amol.deshmukh@infobeans.com")
driver.find_element(By.ID,"pass").send_keys("Ad@#$2023")
driver.find_element(By.NAME,"company").send_keys("Infobeans Technologies")
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

driver.find_element(By.ID,"#cars").click()


