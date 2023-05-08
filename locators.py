from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:/Users/Amol Deshmukh/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

# ID, XPATH, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME,"name").send_keys("Amol D")
driver.find_element(By.NAME,"email").send_keys("amol2050@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,"exampleCheck1").click()

# Xpath - //tagname[@attribute='value']  -> //input[@type='submit']
# CSS - tagname[attribute='value'] -> input[type='submit']  -> #id, .classname <-- all are valid CSS Selectors.


#Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")



driver.find_element(By.CSS_SELECTOR,"label[for='inlineRadio2']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("HelloAgain")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()


print(message)
#driver.implicitly_wait(20)
#driver.close()
