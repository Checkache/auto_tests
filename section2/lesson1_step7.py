from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input_ans = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_ans.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
finally:
    time.sleep(30)
    browser.quit()
    