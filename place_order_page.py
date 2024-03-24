import re

from base_page import BasePage
from page_locators import PlaceOrderPageLocators


class Place_Order_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def set_first_name(self, first_name):
        super().insert_text_by_id(PlaceOrderPageLocators.first_name_field, first_name)

    def set_last_name(self, last_name):
        super().insert_text_by_id(PlaceOrderPageLocators.last_name_field, last_name)

    def set_zip_postal_code(self, zip_postal_code):
        super().insert_text_by_id(PlaceOrderPageLocators.zip_postal_code_field, zip_postal_code)

    def continue_to_checkout_overview(self):
        super().click_element_by_id(PlaceOrderPageLocators.continue_button)

    def fulfill_checkout_informantion(self, first_name, last_name, zip_postal_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_zip_postal_code(zip_postal_code)
        self.continue_to_checkout_overview()


    def get_total_value(self):
        text_n_value = super().get_text_by_class(PlaceOrderPageLocators.summary_subtotal_label)
        value = float(re.search(r'\d+\.\d+', text_n_value).group())
        return value

    def finish_overview(self):
        super().click_element_by_id(PlaceOrderPageLocators.finish_button)

    def get_checkout_status_message(self):
        super().get_text_by_class(PlaceOrderPageLocators.status_message)

    def get_checkout_complete_message(self):
        super().get_text_by_class(PlaceOrderPageLocators.complete_message)