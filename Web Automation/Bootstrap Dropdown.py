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

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")


driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countryList = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countryList))

for country in countryList:
    if country.text == "United Kingdom (UK)":
        country.click()
        break