from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = x_element = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[id=robotCheckbox]").click()
    option1 = browser.find_element_by_css_selector("[id=robotsRule]").click()
    time.sleep(1)
    button = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()

