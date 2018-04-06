from selenium import webdriver
import time



def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def send_input(element="", data="", driver_1):
    
    element = driver.find_element_by_id(element)
    element.click()
    element.send_keys(data)
    element.submit()

def teardown(driver):
    driver.quit()
    print("Driver QUIT..Thank you for using")

element_id = 'lst-ib'
data = 'INDIA'

chrome = driver_chrome()
chrome.get('https:google.co.in')
send_input(element_id, data, driver)
time.sleep(5)
teardown(driver_chrome)



