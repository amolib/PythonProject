from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.CSS_SELECTOR,"input[id='userEmail']").send_keys("amol2050@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("Ad@#$2023")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
#driver.find_element(By.XPATH,"//div[3]//div[1]//div[1]//button[1]").click() #//div[3]//div[1]//div[1]//button[1] #//button[@class='btn w-40 rounded'])[3]
driver.find_element(By.XPATH,"(//button[@class='btn w-10 rounded'])[2]").click()