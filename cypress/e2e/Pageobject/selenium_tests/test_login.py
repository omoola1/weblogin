# login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element(By.ID, 'username')
        self.password_input = driver.find_element(By.ID, 'password')
        self.login_button = driver.find_element(By.ID, 'loginButton')
        self.error_message = driver.find_element(By.ID, 'errorMessage')

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text
