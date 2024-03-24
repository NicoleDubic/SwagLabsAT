import unittest

from selenium import webdriver

from login_failed import LoginFailed
from login_page import LoginPage
from page_locators import LoginPageData


class TestFailedLogin (unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login_page_instance = LoginPage(self.driver)
        self.login_page_instance.open_login_page()
        self.failed_login_page_instance = LoginFailed(self.driver)
        self.login_page_instance.execute_invalid_login()

    def test_url(self):
        expected_url = LoginPageData.log_in_page_url
        actual_url = self.failed_login_page_instance.get_actual_url()
        assert expected_url == actual_url, \
            f"Unexpected URL, expected {expected_url}, but found {actual_url}"

    def test_error_message(self):
        expected_error = LoginPageData.username_password_invalid_expected_message
        actual_error = self.failed_login_page_instance.error_exist()
        assert expected_error == actual_error, \
            f"Unexpected error, expected {expected_error}, but found {actual_error}"

    def tearDown(self) -> None:
        self.driver.quit()