from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Alex")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("Che")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys("123@x.xx")
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    time.sleep(10)
    browser.quit()