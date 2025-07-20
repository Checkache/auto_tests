from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    x = int(x_element.text)
    y = int(y_element.text)
    sum_res = x + y

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_res))
   
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
finally:
    time.sleep(30)
    browser.quit()
    