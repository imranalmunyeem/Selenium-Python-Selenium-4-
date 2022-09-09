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

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

#------------------------------------------Approach 1-Direct input-------------------------------------#

#switch to frame
driver.switch_to.frame(0)

#input date
#driver.find_element(By.ID,'datepicker').send_keys('25/12/1995')

#------------------------------------------Approach 2- Indirect input-------------------------------------#
expectedYear = '2022'
expectedMonth = 'October'
expectedDate = '12'

driver.find_element(By.ID,'datepicker').click()

#compare month and year first
while True:
    actualMonth = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    actualYear =  driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if actualMonth == expectedMonth and actualYear == expectedYear:
        break;
    else:
        driver.find_element(By.XPATH, "//*[id='ui-datepicker-div']/div/a[2]/span").click() #next arrow if doesnt match


#now select date
dates =  driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == expectedDate:
        ele.click()
        break