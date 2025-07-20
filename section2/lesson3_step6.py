from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer" )
    input.send_keys(y)

    btn_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn_submit.click()


finally:
    time.sleep(20)
    browser.quit()
