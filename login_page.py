from base_page import BasePage
from page_locators import LoginPageData, LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def open_login_page(self):
        super().open_url(LoginPageData.log_in_page_url)

    def execute_valid_login(self):
        super().type_text(LoginPageLocators.username_field_xpath, LoginPageData.standard_user)
        super().type_text(LoginPageLocators.password_field_xpath, LoginPageData.users_password)
        super().click(LoginPageLocators.submit_field_xpath)
        

    def execute_invalid_login (self):
        super().type_text(LoginPageLocators.username_field_xpath, LoginPageData.invalid_username)
        super().type_text(LoginPageLocators.password_field_xpath, LoginPageData.invalid_password)
        super().click(LoginPageLocators.submit_field_xpath)



