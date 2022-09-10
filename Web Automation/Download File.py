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

# Open URL
driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()

# Enter text
driver.find_element(By.ID,'textbox').send_keys("Hello world")

# Generate Text File
driver.find_element(By.ID,'createTxt').click()

# Click on Download Button
driver.find_element(By.ID,'link-to-download').click()