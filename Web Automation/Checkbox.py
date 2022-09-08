
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
driver.get("https://formy-project.herokuapp.com/checkbox")


#Verify checkbox is selected or not
checkbox = driver.find_element(By.ID,'checkbox-1')
print('Display Status:' , checkbox.is_selected())

# Check single check box
checkbox.click()
checkbox.click()     #uncheck

#Select multiple checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

#Approach 1
#for i in range(len(checkboxes)):
#    checkboxes[i].click()

#Approach 2
#for checkbox in checkboxes:
   # checkbox.click();

#Select multiple checkboxes by choice
# for checkbox in checkboxes:
#     checkboxID= checkboxes.get_attribute('id')
#     if checkboxID == 'checkbox-1' or checkboxID == 'checkbox-2' or checkboxID == 'checkbox-3':
#         checkbox.click()

#Select last 2 checkbox
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click();

#Select first 2 checkbox
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()