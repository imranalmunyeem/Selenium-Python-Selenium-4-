import requests
#Make sure your chrome driver version matches with the your chrome browser

#Selenium 3 driver import format
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 3 locator finding format
# driver.find_element_by_id ('id')

#import requests to get broken links

#Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)

driver.get("https://amazon.com/")

# find web links
link = driver.find_elements(By.TAG_NAME, 'a')

# using len function count how many links
print(len(link))


#print all the link name
for linkname in link:
    print(linkname.text)

#get all links
allLinks = driver.find_elements(By.TAG_NAME, 'a')



#check each link if it is broken or not
count = 0

for link in allLinks:
    #extract url from href attribute
    url = link.get_attribute('href')

    #send request to the url and get the result
    result = requests.head(url)

    #if status code is not 200 then print the url (customize the if condition according to the need)
    if result.status_code >= 400:
        print(url, "is broken link")
        count +=1