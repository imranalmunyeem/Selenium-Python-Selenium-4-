# This web page is divided into three frames, left top (1st frame) and left bottom(2nd frame) and the third frame. All the frames interconnected. Then we perform these actions by selenium:
#
# First of all, switch to the default frame to the first frame.
# Then find the element using link text method
# Go back to the default frame.
# Then go to the 2nd frame
# Find element using the link text method
# Go back to the default frame
# Then switch to the 3rd frame.
# Then find element by x path.
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

# web page url
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

# switch to 1st frame
driver.switch_to.frame("packageListFrame")

# click on 1st frame
driver.driver.find_element(By.LINK_TEXT,"org.openqa.selenium.opera").click()

# back to default web page frame
driver.switch_to.default_content()

# switch to 2nd frame
driver.switch_to.frame("packageFrame")

# click on 2nd frame
driver.find_element(By.LINK_TEXT,"OperaOptions").click()

# back to default web page frame
driver.switch_to.default_content()

# switch to 3rd frame
driver.switch_to.frame("classFrame")

# click on 2nd frame
driver.find_element(By.XPATH,'/html/body/div[1]/ul/li[4]/a').click()
time.sleep(4)
