from base_page import BasePage
from page_locators import LoginPageLocators, LoginPageData


class LoggedInSuccesfully(BasePage, LoginPageData, LoginPageLocators):
    def __init__(self, driver):
        super().__init__(driver)

    def get_actual_url(self):
        return super().get_current_url()

    def get_header_message(self):
        return super().get_text(LoginPageLocators.logged_in_successfully_xpath)

    def is_logout_button_displayed(self):
        return super().is_object_displayed(LoginPageLocators.log_out_button_link)