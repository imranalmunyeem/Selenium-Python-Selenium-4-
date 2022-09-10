#Make sure your chrome driver version matches with the your chrome browser
import sys

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

#to identify element
s = driver.find_element(By.XPATH,"//input[@type='file']")

#file path specified with send_keys
s.send_keys("C:\Users\Pictures\Logo.jpg")