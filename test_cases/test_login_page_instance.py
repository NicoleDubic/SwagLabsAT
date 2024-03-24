import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from login_page import LoginPage
from login_successfully import LoggedInSuccesfully
from page_locators import LoginPageData


class TestLoginPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login_page_instance = LoginPage(self.driver)
        self.login_page_instance.open_login_page()

    def test_url (self):

        actual_url = self.login_page_instance.get_current_url()
        expected_url = LoginPageData.log_in_page_url
        time.sleep(4)
        assert actual_url == expected_url, \
            f"Unexpected URL, expected {expected_url}, but found {actual_url}"

    def test_title (self):
        expected_title = LoginPageData.login_page_title
        actual_title = self.login_page_instance.get_title()
        assert actual_title == expected_title, \
            f"Unexpected title, expected {expected_title}, but found {actual_title}"

    def tearDown(self) -> None:
        self.driver.quit()
