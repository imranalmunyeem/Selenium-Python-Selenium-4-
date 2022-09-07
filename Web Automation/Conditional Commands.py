
#Make sure your chrome driver version matches with the your chrome browser

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)
driver.get("https://admin-demo.nopcommerce.com/login")

#is displayed () / is enabled () / is_selected()
checkbox = driver.find_element(By.XPATH,'//*[@id="RememberMe"]')
print('Display Status:' , checkbox.is_displayed())
print('Display Status:' , checkbox.is_enabled())
print('Display Status:' , checkbox.is_selected())