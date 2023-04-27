from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service_obj)

driver.get("https://www.surveymonkey.com/")
driver.find_element(By.CLASS_NAME,"wds-button--upgrade").click()
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("catejah957@meidecn.com")
driver.find_element(By.XPATH,"//input[@id='tou-checkbox']").click()
driver.find_element(By.XPATH,"//input[@id='privacy-checkbox']").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.ID,"password").send_keys("Inf@1238#12")
driver.find_element(By.ID,"password1").send_keys("Inf@1238#12")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
