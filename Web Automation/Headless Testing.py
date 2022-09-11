#Make sure your chrome driver version matches with the your chrome browser

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver

#--------------------------------------Chrome Browser----------------------------------------#
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


#--------------------------------------Mozila Firefox Browser----------------------------------------#
def headless_edge():
    from selenium.webdriver.edge.service import Service
    service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\IEDriverServer.exe")
    option=webdriver.EdgeOptions()
    option.headless=True
    driver =webdriver.Edge(service = service_Object,options=option)
    return driver

driver=headless_edge()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()


#--------------------------------------IE Browser----------------------------------------#
def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\geckodriver.exe")
    option=webdriver.FirefoxOptions()
    option.headless=True
    driver =webdriver.Firefox (service = service_Object,options=option)
    return driver

driver=headless_firefox()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()