from pages.base_page import BasePage
from pages.page_locators import LoginPageData, LoginPageLocators


class LoginFailed (BasePage, LoginPageData, LoginPageLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def get_actual_url(self):
        return super().get_current_url()

    def error_exist(self):
        return super().get_text(LoginPageLocators.logged_in_failed_xpath)