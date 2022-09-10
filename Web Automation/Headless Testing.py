#Make sure your chrome driver version matches with the your chrome browser

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")
    option=webdriver.ChromeOptions()
    option.headless=True
    driver =webdriver.Chrome (service = service_Object,options=option)
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()