from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsOpen = driver.window_handles

driver.switch_to.window(windowsOpen[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.switch_to.window(windowsOpen[0])

assert "Opening a new window" == print(driver.find_element(By.TAG_NAME,"h3").text)



