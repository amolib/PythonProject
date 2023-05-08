import time
import pyautogui


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
#print(count)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
