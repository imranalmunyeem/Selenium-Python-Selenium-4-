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
             --- Every element does not	have an	id->static id, unique name, unique link text. For those	elements we need to build xpath	to find	and then perform actions on them.
             --- Difference between single ‘/’ or double ‘//’
                --- Single slash ‘/’: anywhere in xpath	signifies to look for the element immediately inside the parent	element.
                --- Double slash ‘//’ signifies	to look	for any	child or nested child element inside the parent	element.
                --- Syntax:
                        //tag[@attribute='value']
                        
                        Relative xpath using single ‘/’	for Login link:
                                //div[@id='navbar']/div/div/div/ul/li[2]/a
                                
                        Relative xpath using double ‘//’ for Login link:
                                //div[@id='navbar']//ul/li[2]/a    
                                
                        Don’t use “*”, always use the tag name.
                        
                        Using Text of the element to build xpath
                        Finding	Login	link:
                                //div[@class='homepage-hero']//a[text()='Enroll	now']
                        
                        Using Contains to find the elements:
                                Syntax: //tag[contains(attribute, ‘value’)]
                                
                        Finding	Login	link:
                                //div[@id='navbar']//a[contains(text(),'Login')]
                                //div[@id='navbar']//a[contains(@class,'navbar-link') and contains(@href,'sign_in')]
                                
                        Using Starts-With to find the elements:
                                Syntax:	//tag[starts-with(attribute,	‘value’)]
                                
                        Finding	Login link:
                                //div[@id='navbar']//a[starts-with(@class,'navbar-link')]
                                
                        Parent
                                Syntax:	xpath-to-some-element//parent::<tag>
                                
                        Preceding Sibling
                                Syntax:	xpath-to-some-element//preceding-sibling::<tag>
                                
                        Following Sibling
                                Syntax:	xpath-to-some-element//following-sibling::<tag>
                         
                        
### ⚫ The difference between quit() and close()?
                --- driver.quit(): The quit() method quits the driver, closing every associated window.

                --- driver.close(): The close() method closes the currently focused window, quitting the driver if the current window is the only open window. If there are no windows open, it will error out.
                
      
### ⚫ Difference between findElement and findElements Methods?  
                --- FindElement() Method:
                        --- This command is used to access any single element on the web page
                        --- It will return the object of the first matching element of the specified locator
                        --- It will throw NoSuchElementException when it fails to identify the element
                        
                --- FindElements() Method:
                        --- This command is used to uniquely identify the list of web elements within the web page.
                        --- The usage of this method is very limited
                        --- If the element doesn’t exist on the page then, then it will return value with an empty list


### ⚫ Difference b/w getText() and getAttribute() in Selenium WebDriver? 
                 --- The getText() Method
                        --- The getText() method returns the innerText of an element
                        
                 --- The getAttribute() Method
                        --- The getAttribute() method fetches the text contained by an attribute in an HTML document. It returns the value of the HTML element's attribute as a string.                       


### ⚫ Difference b/w implicit, explicit, and fluent wait?
                 --- Implicit wait:
                        --- An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. 
                        --- The default setting is 0. Once set, the implicit wait is set for the life of the WebDriver object.
                        --- Advantage:
                                --- Single statement
                                --- Will not reduce the performance. If the element is available within the time it will execute the further statements.
                        --- Disadvantage: 
                                --- Implicit wait will work for every statements written in the code.
                                --- If the element is not available within the time mentioned, still there is a chance to get the exception. [N.B: Using try catch block we can solve this issue. In that case, program will still run even after getting the exception]
                        
                 --- Explicit wait: 
                        --- To use explicit wait you have to import WebDriverWait and Expected condition
                        --- An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. 
                        --- The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait.
                        --- Advantage:
                                --- Explicit wait is based on condition.
                                --- Effective than other types of wait.
                                --- We can add poll frequency []
                         --- Disavantage 
                                --- Complicated because have to place it to multiple places.
                        
                 --- Fluent wait:
                        --- FluentWait defines the maximum amount of time to wait for a condition, as well as the frequency with which to check the condition.
                        --- It also defines how frequently WebDriver will check if the condition appears before throwing the “ElementNotVisibleException”.
                        --- Fluent Wait looks for a web element repeatedly at regular intervals until timeout happens or until the object is found.
                        --- Fluent Wait commands are most useful when interacting with web elements that can take longer durations to load. This is something that often occurs in Ajax applications.
                        --- While using Fluent Wait, it is possible to set a default polling period as needed. The user can configure the wait to ignore any exceptions during the polling period.
                        --- Fluent waits are also sometimes called smart waits because they don’t wait out the entire duration defined in the code. Instead, the test continues to execute as soon as the element is detected – as soon as the condition specified in .until(YourCondition) method becomes true.
                        --- Python API does not have a FluentWait class, but it kind of supports it with keyworded arguments.
