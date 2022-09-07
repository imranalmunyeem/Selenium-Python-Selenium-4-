
#Make sure your chrome driver version matches with the your chrome browser

#Selenium 3 driver import format
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 3 locator finding format
# driver.find_element_by_id ('id')

#Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)

driver.get("https://admin-demo.nopcommerce.com/login")

#input email
adminEmail = driver.find_element(By.ID,'Email')
adminEmail.clear()                              #Clear clear the input box first
adminEmail.send_keys('admin@yourstore.com')      #Send keys will input values

#input password
adminPassword = driver.find_element(By.ID,'Password')
adminPassword .clear()
adminPassword .send_keys('admin')

#click on login
loginButton = driver.find_element(By.CLASS_NAME,'button-1')
loginButton.click()


#click on logout
logoutButton = driver.find_element(By.LINK_TEXT,'Logout')
logoutButton.click()