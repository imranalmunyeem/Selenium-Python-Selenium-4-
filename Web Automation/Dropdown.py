
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

#click on birthday dropdown using Select
birthdayDropdown = driver.find_element(By.NAME,'DateOfBirthDay')
birthdayDropdown = Select (birthdayDropdown)

#select by value
birthdayDropdown.select_by_value('25')

#click on birthmonth using Select
birthmonthDropdown = driver.find_element(By.NAME,'DateOfBirthMonth')
birthmonthDropdown = Select (birthmonthDropdown)

#select by visible text
birthmonthDropdown.select_by_visible_text('December')


#click on birthmonth using Select
birthyearDropdown = driver.find_element(By.NAME,'DateOfBirthYear')
birthyearDropdown = Select (birthyearDropdown)

#select by index
birthyearDropdown.select_by_index('84')

#dynamic dropdown without using any built-in function
allOptions = birthyearDropdown.options
print('Total number of options:', len(allOptions))

for opt in allOptions:
    print(opt.text)

for opt in allOptions:
    if opt.text == '1992':
        opt.click()
