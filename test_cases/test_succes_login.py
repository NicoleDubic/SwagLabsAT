import unittest

from selenium import webdriver

from login_page import LoginPage
from login_successfully import LoggedInSuccesfully
from page_locators import LoginPageData, LoginPageLocators


class TestPositiveLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login_page_instance = LoginPage(self.driver)
        self.login_page_instance.open_login_page()
        self.success_login_page_instance = LoggedInSuccesfully(self.driver)
        self.login_page_instance.execute_valid_login()


    def test_valide_login_url(self):
        expected_url = LoginPageData.successfully_logged_in_url
        actual_url = self.success_login_page_instance.get_actual_url()
        assert expected_url == actual_url, \
            f"Unexpected URL, expected {expected_url}, but found {actual_url}"

    def test_valide_login_title(self):
        expected_title = LoginPageData.login_page_title
        actual_title = self.success_login_page_instance.login_page_title
        assert expected_title == actual_title, \
            f"Unexpected URL, expected {expected_title}, but found {actual_title}"

    def test_logout_button (self):
        self.success_login_page_instance.click(LoginPageLocators.burger_menu_button)
        expected_result = True
        actual_result = self.success_login_page_instance.is_logout_button_displayed()
        assert expected_result == actual_result, \
            f"Unexpected result, expected {expected_result}, but found {actual_result}"


    def tearDown(self) -> None:
        self.driver.quit()
