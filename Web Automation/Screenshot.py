#Make sure your chrome driver version matches with the your chrome browser
import os
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

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#-----------------------------------------------approach 1-------------------------------------#
driver.save_screenshot("C:\\Users\\ialmu\\PycharmProjects\\Selenium-Python (Selenium 4)\\screenshots\\screenshot1.png")
#driver.save_screenshot(os.getcwd()+"\\screenshot1.png")  #we can use os.getcwd instead of full path

# #-----------------------------------------------approach 2-------------------------------------#
# driver.get_screenshot_as_file("C:\\Users\\ialmu\\PycharmProjects\\Selenium-Python (Selenium 4)\\screenshots\\screenshot1.png")
# #driver.save_screenshot(os.getcwd()+"\\screenshot1.png")  #we can use os.getcwd instead of full path
#
#
# #-----------------------------------------------approach 3-------------------------------------#
# driver.get_screenshot_as_png("C:\\Users\\ialmu\\PycharmProjects\\Selenium-Python (Selenium 4)\\screenshots\\screenshot1.png")
# #driver.save_screenshot(os.getcwd()+"\\screenshot1.png")  #we can use os.getcwd instead of full path
#
# #-----------------------------------------------approach 4-------------------------------------#
# driver.get_screenshot_as_base64("C:\\Users\\ialmu\\PycharmProjects\\Selenium-Python (Selenium 4)\\screenshots\\screenshot1.png") #save in binary format
# #driver.save_screenshot(os.getcwd()+"\\screenshot1.png")  #we can use os.getcwd instead of full path
