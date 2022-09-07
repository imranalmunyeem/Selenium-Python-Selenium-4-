# Web automation using Selenium 4
### Make sure your chrome driver version matches with the your chrome browser


### Selenium 3 driver import format
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")
    

### Selenium 4 driver import format
  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service

  service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")
  driver =webdriver.Chrome (service = service_Object)
  
  
### Selenium 3 find element format 
  driver.find_element_by_id ('id')
  
  
### Selenium 4 find element format
  from selenium.webdriver.common.by import By
  driver.find_element(By.ID,'Email')
