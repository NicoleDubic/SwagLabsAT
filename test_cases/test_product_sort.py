import time
import unittest
from selenium import webdriver

from pages.inventory_page import Inventory_Page
from pages.login_page import LoginPage
from pages.login_successfully import LoggedInSuccesfully



class TestSort(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login_page_instance = LoginPage(self.driver)
        self.login_page_instance.open_login_page()
        self.success_login_page_instance = LoggedInSuccesfully(self.driver)
        self.login_page_instance.execute_valid_login()
        self.inventory_page_instance = Inventory_Page(self.driver)

    def test_default_items_sort(self):
        items_titles = self.inventory_page_instance.get_inventory_items_titles()
        time.sleep(3)
        sorted_items_titles = items_titles.copy()
        sorted_items_titles.sort()
        self.assertListEqual(items_titles, sorted_items_titles, "Items are not in a correct order")

    def test_sort_Z_to_A(self):
        self.inventory_page_instance.select_sort_type_by_text("Name (Z to A)")

        items_titles = self.inventory_page_instance.get_inventory_items_titles()
        reverse_items_titles = items_titles.copy()
        reverse_items_titles.sort()
        reverse_items_titles.reverse()
        self.assertListEqual(items_titles, reverse_items_titles, "Items are not sorted Z to A")

    def test_sort_price_low_high(self):
        self.inventory_page_instance.select_sort_type_by_text('Price (low to high)')
        item_prices = self.inventory_page_instance.get_inventory_items_prices()
        sorted_item_prices = item_prices.copy()
        sorted_item_prices.sort()
        self.assertListEqual(item_prices, sorted_item_prices, "Prices are not sorted low to high")

    def test_sort_price_high_low(self):
        self.inventory_page_instance.select_sort_type_by_text('Price (high to low)')
        item_prices = self.inventory_page_instance.get_inventory_items_prices()
        sorted_item_prices = item_prices.copy()
        sorted_item_prices.sort()
        sorted_item_prices.reverse()
        self.assertListEqual(item_prices, sorted_item_prices, "Prices are not sorted high to low")


    def tearDown(self) -> None:
        self.driver.quit()
