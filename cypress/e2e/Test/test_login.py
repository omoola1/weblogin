# test_login.py
import unittest
from selenium import webdriver
from login_page import LoginPage

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://yourapp.com/login')
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        self.login_page.login('validUser', 'validPassword')
        self.assertEqual(self.driver.current_url, 'https://yourapp.com/dashboard')

    def test_failed_login(self):
        self.login_page.login('invalidUser', 'invalidPassword')
        self.assertTrue(self.login_page.get_error_message().is_displayed())

    def test_error_message_display(self):
        self.login_page.login('invalidUser', 'invalidPassword')
        error_message = self.login_page.get_error_message()
        self.assertIn('Invalid username or password', error_message)

if __name__ == '__main__':
    unittest.main()
