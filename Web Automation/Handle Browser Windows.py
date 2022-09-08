
#Make sure your chrome driver version matches with the your chrome browser

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

driver.find_element(By.XPATH,'/html/body/div[6]/div[4]/div[1]/div[4]/div[1]/ul/li[2]/a').click()


#--------------------------------------Approach 1---------------------------------------------#
#switch from one window to another window
windowsIDs = driver.window_handles
parentWindowID = windowsIDs[0]
childWindowID = windowsIDs[1]

#print(parentWindowID, childWindowID)
driver.switch_to.window(childWindowID)
print("Parent window is", driver.title)

driver.switch_to.window(parentWindowID)
print("Child window is",driver.title)


#--------------------------------------Approach 2---------------------------------------------#
for windowID in windowsIDs:
        driver.switch_to.window(windowID)
        print(driver.title)

#--------------------------------------Close specific browser window---------------------------------------------#
for windowID in windowsIDs:
        driver.switch_to.window(windowID)
        if driver.title == "nopCommerce demo store. Register" or driver.title == "twitter"
            driver.close()