from selenium import webdriver
import time

def send_input(element="", data=""):
    global driver

    element = driver.find_element_by_id(element)
    element.click()
    element.send_keys(data)
    element.submit()

def teardown():
    global driver
    driver.quit()
    print("Driver QUIT..Thank you for using")

element_id = 'lst-ib'
data = 'INDIA'

driver = webdriver.Chrome()
driver.get('https:google.co.in')
driver.maximize_window()
send_input(element_id, data)
time.sleep(5)
teardown()



