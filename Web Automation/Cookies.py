#Make sure your chrome driver version matches with the your chrome browser
import os
import sys

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


#capture cookies from browser
cookies = driver.get_cookies()
print("Size of cookies:",len(cookies))

#print details of all the cookies
for cookie in cookies:
    print(cookie)
    print(cookie.get('name'),":",cookie.get('value'))


#Add new cookie
driver.add_cookie({"name":"Imran","value":"123456"})
cookies = driver.get_cookies()       #have to run this again since we added new cookie
print("Size of new cookies:",len(cookies))

#delete specific cookie from browswe
driver.delete_cookie("Imran")
cookies = driver.get_cookies()
print("Size of new cookies after deletion:",len(cookies))

#delete specific cookie from browswe
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of new cookies after deletion:",len(cookies))