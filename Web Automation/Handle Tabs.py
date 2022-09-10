#Make sure your chrome driver version matches with the your chrome browser
import os
import sys

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# open registration page in another tab
registrationLink = Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(registrationLink)


# open both website at the same time in different tabs
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('tab')                  #Selenium 4 feature
driver.get("https://amazon.com/")


# open both website at the same time in different window
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')                  #Selenium 4 feature
driver.get("https://amazon.com/")