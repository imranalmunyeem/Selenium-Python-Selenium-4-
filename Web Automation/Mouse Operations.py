#only 3 actions that can be accomplished with a mouse: pressing down on a button, releasing a pressed button, and moving the mouse.

#Make sure your chrome driver version matches with the your chrome browser

#Selenium 3
    #from selenium import webdriver
    #driver = webdriver.Chrome(executable_path= "C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

#Selenium 4
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By

service_Object = Service("C:\\Users\\ialmu\\PycharmProjects\\Drivers\\chromedriver.exe")

driver =webdriver.Chrome (service = service_Object)

driver.get("url")

#This method combines moving the mouse to the center of an element with pressing the left mouse button. This is useful for focusing a specific element
clickable = driver.find_element(By.ID, "clickable")
ActionChains(driver) \
    .click_and_hold(clickable) \
    .perform()


#This method combines moving to the center of an element with pressing and releasing the left mouse button. This is otherwise known as “clicking”
clickable = driver.find_element(By.ID, "click")
ActionChains(driver)\
        .click(clickable)\
        .perform()


#This method combines moving to the center of an element with pressing and releasing the right mouse button (button 2). This is otherwise known as “right-clicking
clickable = driver.find_element(By.ID, "clickable")
ActionChains(driver) \
    .context_click(clickable) \
    .perform()


# Back Click
# There is no convenience method for this, it is just pressing and releasing mouse button 3
action = ActionBuilder(driver)
action.pointer_action.pointer_down(MouseButton.BACK)
action.pointer_action.pointer_up(MouseButton.BACK)
action.perform()


# Forward Click
# There is no convenience method for this, it is just pressing and releasing mouse button 4
action = ActionBuilder(driver)
action.pointer_action.pointer_down(MouseButton.FORWARD)
action.pointer_action.pointer_up(MouseButton.FORWARD)
action.perform()


# Double click
# This method combines moving to the center of an element with pressing and releasing the left mouse button twice.
clickable = driver.find_element(By.ID, "clickable")
ActionChains(driver) \
    .double_click(clickable) \
    .perform()


# Move to element
# This method moves the mouse to the in-view center point of the element. This is otherwise known as “hovering.” Note that the element must be in the viewport or else the command will error.
hoverable = driver.find_element(By.ID, "hover")
ActionChains(driver) \
    .move_to_element(hoverable) \
    .perform()


# Offset from Element (Top Left Origin)
# This method moves the mouse to the in-view center point of the element then attempts to move to the upper left corner of the element and then moves by the provided offset.
mouse_tracker = driver.find_element(By.ID, "mouse-tracker")
ActionChains(driver) \
    .move_to_element_with_offset(mouse_tracker, 8, 0) \
    .perform()


#Offset from Viewport
action = ActionBuilder(driver)
action.pointer_action.move_to_location(8, 0)
action.perform()


# Offset from Current Pointer Location
# This method moves the mouse from its current position by the offset provided by the user. If the mouse has not previously been moved, the position will be in the upper left corner of the viewport. Note that the pointer position does not change when the page is scrolled.
# Note that the first argument X specifies to move right when positive, while the second argument Y specifies to move down when positive. So moveByOffset(30, -10) moves right 30 and up 10 from the current mouse position.
ActionChains(driver) \
    .move_by_offset(13, 15) \
    .perform()


#Drag and Drop on Element
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")
ActionChains(driver) \
    .drag_and_drop(draggable, droppable) \
    .perform()

# Drag and Drop by Offset
# This method firstly performs a click-and-hold on the source element, moves to the given offset and then releases the mouse.
draggable = driver.find_element(By.ID, "draggable")
start = draggable.location
finish = driver.find_element(By.ID, "droppable").location
ActionChains(driver) \
    .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y']) \
    .perform()