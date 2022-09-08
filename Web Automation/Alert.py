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
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#------------------------------JS Alert----------------------------
# Handling alert

#open alert
jsAlert = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button')
jsAlert.click();
time.sleep(2)

#switch to alert

alertWindow1 = driver.switch_to.alert
#click on ok
alertWindow1.accept()

#------------------------------JS Confirm----------------------------
#open alert
jsConfirm = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button')
jsConfirm.click();
time.sleep(2)

#switch to alert

alertWindow2 = driver.switch_to.alert
#click on ok
alertWindow2.dismiss()


#------------------------------JS Prompt----------------------------
#open alert
jsPrompt = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button')
jsPrompt.click()
time.sleep(2)

#switch to alert

alertWindow3 = driver.switch_to.alert

#Send value
print(alertWindow3.text)
alertWindow3.send_keys("Testing the prompt")