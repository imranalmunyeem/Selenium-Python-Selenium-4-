
#Make sure your chrome driver version matches with the your chrome browser

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)
driver.get("https://www.orangehrm.com/")