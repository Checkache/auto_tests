import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        time.sleep(1)
        self.browser.quit()

    def fill_form_and_submit(self, url):
        browser = self.browser
        browser.get(url)

        # Заполняем обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test@example.com")

        # Отправляем форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Ждём загрузки новой страницы
        time.sleep(1)

        # Ищем элемент с текстом
        return browser.find_element(By.TAG_NAME, "h1").text

    def test_registration1(self):
        result_text = self.fill_form_and_submit("http://suninjuly.github.io/registration1.html")
        self.assertEqual(result_text, "Congratulations! You have successfully registered!", "registration1 failed")

    def test_registration2(self):
        result_text = self.fill_form_and_submit("http://suninjuly.github.io/registration2.html")
        self.assertEqual(result_text, "Congratulations! You have successfully registered!", "registration2 failed")

if __name__ == "__main__":
    unittest.main()
