from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    y = str(int(num1) + int(num2))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(y)
    button = browser.find_element_by_class_name("btn").click()

finally:

    time.sleep(5)
    browser.quit()