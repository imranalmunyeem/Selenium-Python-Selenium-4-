# 1) Count number of rows and columns
# 2) Read specific row and column data
# 3) Read specific row and column data
# 3) Read data based on confitions ( like author and others)


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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# Count number of rows and columns from a table
totalRow = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody//tr")  #total row
print(len(totalRow))

totalColumn = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody//tr/th")  #total comumn
print(len(totalColumn))


# Read specific row and column data
specificData = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(specificData)



# Read specific row and column data
for row in range(2,totalRow+1):  #here we used totalR+1 because row is always n-1 by default, so we have to cout=nt the last row also by adding +1
    for column in range(1, totalColumn+1):
        allData = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(column)+"]").text  #injected this custom tr["+str(row)+"]/td["+str(column)+"] variable in xpath; it will automatically change the row and column data
        print(allData)


# Read data based on confitions ( like author and others)
for row in range(2,totalRow+1):  #here we used totalR+1 because row is always n-1 by default, so we have to cout=nt the last row also by adding +1
        authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text  #injected this custom tr["+str(row)+"]/td["+str(column)+"] variable in xpath; it will automatically change the row and column data
        if authorName == "Mukesh":
            bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]").text
            print(bookName,"        ",authorName)

driver.close()