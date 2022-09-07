# Web automation using Selenium 4
### Make sure your chrome driver version matches with the your chrome browser


### ⚫ Selenium 3 driver import format
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")
    

### ⚫ Selenium 4 driver import format
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service

        service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")
        driver =webdriver.Chrome (service = service_Object)
  
  
### ⚫ Selenium 3 find element format 
        driver.find_element_by_id ('id')
  
  
### ⚫ Selenium 4 find element format
        from selenium.webdriver.common.by import By
        driver.find_element(By.ID,'Email')


### ⚫ How to locate elements?
            --- driver.find_element(By.ID, "id")
            
            --- driver.find_element(By.NAME, "name")
            
            --- driver.find_element(By.XPATH, "xpath")
            
            --- driver.find_element(By.LINK_TEXT, "link text")
            
            --- driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
            
            --- driver.find_element(By.TAG_NAME, "tag name")
            
            --- driver.find_element(By.CLASS_NAME, "class name")
            
            --- driver.find_element(By.CSS_SELECTOR, "css selector")
 

#### ⚫ What is XPath?
            --- XPath stands for XML Path Language	
            --- XPath uses "path like" syntax to identify and navigate nodes in an XML document


#### ⚫ Types of XPath?
            --- Absolute XPath:
                        --- It is the direct way to find the element, but the disadvantage of the absolute XPath is that if there are any changes made in the path of the element then that XPath gets failed.
                        
                        --- The key characteristic of XPath is that it begins with the single forward slash(/) ,which means you can select the element from the root node.
                        
                        --- Example: /html/body/div[2]/div[1]/div/h4[1]/b/html[1]/body[1]/div[2]/div[1]/div[1]/h4[1]/b[1]
                        
            --- Relative XPath: 
                        --- Relative Xpath starts from the middle of HTML DOM structure.
                        
                        --- It starts with double forward slash (//). 
                        
                        --- It can search elements anywhere on the webpage, means no need to write a long xpath and you can start from the middle of HTML DOM structure.    
                        
                        --- Relative Xpath is always preferred as it is not a complete path from the root element.
                        
                        --- Example: //div[@class='featured-box cloumnsize1']//h4[1]//b[1]
                        
                        
 ### ⚫ How to make custom XPATH?
 
 
