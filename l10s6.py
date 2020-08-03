from selenium import webdriver
import time
import math

try:

    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id("button")


finally:
    time.sleep(5)
    browser.quit()