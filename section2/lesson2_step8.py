from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
import os

fake = Faker()

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys(fake.first_name())
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys(fake.last_name())
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys(fake.email())

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn") 
    button.click()
finally:
    time.sleep(30)
    browser.quit()
    