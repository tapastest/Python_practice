import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


capabilities = {
    'browserName': 'Chrome',
    'platformName': 'Android',
    'deviceName': 'ZY223SHVJW',
    'platformVersion': '7.0'
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

data = 'INDIA'

driver.get('http://google.co.in')
#div = driver.find_element_by_xpath("//android.widget.EditText[@bounds='[22,718][872,781]']")
sin = driver.find_element_by_link_text("Sign in").click()
#div.send_keys(data)
#div.submit()

actions = TouchActions(driver)
actions.tap(element)
actions.perform()



time.sleep(7)
# close the driver
driver.quit()

