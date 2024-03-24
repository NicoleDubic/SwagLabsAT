from base_page import BasePage
from page_locators import InventoryPageLocators


class Inventory_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_inventory_items_titles(self):
        return super().get_items_titles(InventoryPageLocators.items_titles)

    def get_inventory_items_prices(self):
        return super().get_items_prices(InventoryPageLocators.items_prices)

    def get_inventory_item_title_by_index(self, index):
        return super().get_items_titles(InventoryPageLocators.inventory_item_name)[index]

    def get_inventory_item_price_by_index(self, index):
        return super().get_items_prices(InventoryPageLocators.inventory_item_price)[index]
    def add_item_to_cart_by_index(self, index):
        return super().get_buttons_list_by_xpath(InventoryPageLocators.inventory_item_button)[index].click()

    def select_sort_type_by_text(self, visible_text_option):
        return super().select_by_visible_text(InventoryPageLocators.select_product_sort_container, visible_text_option)

    def get_sort_type_text(self):
        return super().get_visible_text_selected(InventoryPageLocators.get_product_sort_container)




    def access_cart(self):
        super().click_element_by_class(InventoryPageLocators.shopping_cart_button)

    def go_to_checkout(self):
        super().click_element_by_xpath(InventoryPageLocators.checkout_button)