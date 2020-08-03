from selenium import webdriver
import time
import math

try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button").click


finally:
    time.sleep(5)
    browser.quit()