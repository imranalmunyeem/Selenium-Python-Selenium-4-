#Make sure your chrome driver version matches with the your chrome browser
import sys

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)

driver.get("url")
driver.maximize_window()

#Copy and Paste
cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

ActionChains(driver) \
    .send_keys("Selenium!") \
    .send_keys(Keys.ARROW_LEFT) \
    .key_down(Keys.SHIFT) \
    .send_keys(Keys.ARROW_UP) \
    .key_up(Keys.SHIFT) \
    .key_down(cmd_ctrl) \
    .send_keys("xvv") \
    .key_up(cmd_ctrl) \
    .perform()


#Designated Element
text_input = driver.find_element(By.ID, "textInput")
ActionChains(driver) \
    .send_keys_to_element(text_input, "abc") \
    .perform()


#Send keys
ActionChains(driver) \
    .send_keys("abc") \
    .perform()


#Key up
ActionChains(driver) \
    .key_down(Keys.SHIFT) \
    .send_keys("a") \
    .key_up(Keys.SHIFT) \
    .send_keys("b") \
    .perform()


#Key down
ActionChains(driver) \
    .key_down(Keys.SHIFT) \
    .send_keys("abc") \
    .perform()