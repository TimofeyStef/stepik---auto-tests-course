from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("input_value").text
    y = int(num1)
    num2 = str(math.log(abs(12*math.sin(y))))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(num2)
    option1 = browser.find_element_by_css_selector("[id=robotCheckbox]").click()
    option2 = browser.find_element_by_css_selector("[id=robotsRule]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()