import time

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

# set implicit wait time
driver.implicitly_wait(10)  # seconds #implicit wait will work for every statements

# get geeksforgeeks.org
driver.get("https://demo.nopcommerce.com/")

# get element after 10 seconds
element = driver.find_element(By.LINK_TEXT,'Gift Cards ')

# click element
element.click()

