from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    y = int(browser.find_element_by_id("input_value").text)
    x = str(math.log(abs(12 * math.sin(y))))
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(x)
    button = browser.find_element_by_tag_name("button").click()


finally:
    time.sleep(5)
    browser.quit()
