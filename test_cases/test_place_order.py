import random
import time
import unittest
from selenium import webdriver
from inventory_page import Inventory_Page
from login_page import LoginPage
from login_successfully import LoggedInSuccesfully
from page_locators import PlaceOrderPageData
from place_order_page import Place_Order_Page


class Test_Place_Order(unittest.TestCase):
    #define the global variable
    products_in_cart = []

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login_page_instance = LoginPage(self.driver)
        self.login_page_instance.open_login_page()
        self.success_login_page_instance = LoggedInSuccesfully(self.driver)
        self.login_page_instance.execute_valid_login()
        self.inventory_page_instance = Inventory_Page(self.driver)
        self.place_order_page_instance = Place_Order_Page(self.driver)
        self.products_in_cart = []

    def test_add_items_to_cart(self):
        product_index_first = random.randint(0,5)
        self.inventory_page_instance.add_item_to_cart_by_index(product_index_first)
        product_index_second = random.randint(0, 5)
        if product_index_first == product_index_second:
            product_index_second = random.randint(0,5)
        self.inventory_page_instance.add_item_to_cart_by_index(product_index_second)

        for product_index in [product_index_first, product_index_second]:
            product_title = self.inventory_page_instance.get_inventory_item_title_by_index(product_index)
            product_price = self.inventory_page_instance.get_inventory_item_price_by_index(product_index)
            self.products_in_cart.append({
                "index": product_index,
                "title": product_title,
                "price": product_price
            })
        cart_item_titles = self.inventory_page_instance.get_inventory_items_titles()
        cart_item_prices = self.inventory_page_instance.get_inventory_items_prices()

        # Assert to verify if products are added to the cart
        for product in self.products_in_cart:
            assert product["title"] in cart_item_titles, \
                f"Product title {product['title']} not found in cart"
            assert product["price"] in cart_item_prices, \
                f"Product price {product['price']} not found in cart"

    #checkout flow
    def test_verify_cart(self):
        self.test_add_items_to_cart()
        self.inventory_page_instance.access_cart()
        total_value = 0
        time.sleep(4)
        for product in self.products_in_cart:
            self.assertIn(
                product["title"],
                self.inventory_page_instance.get_inventory_items_titles()
            )

            self.assertIn(
                product["price"],
                self.inventory_page_instance.get_inventory_items_prices()
            )

            total_value += product["price"]

            # checkout
        self.inventory_page_instance.go_to_checkout()

        # fulfill checkout
        self.place_order_page_instance.fulfill_checkout_informantion(PlaceOrderPageData.first_name, PlaceOrderPageData.last_name, PlaceOrderPageData.zip_postal_code)

        # validate total price without tax
        self.assertEqual(
            self.place_order_page_instance.get_total_value(),
            total_value,
            'Total item values without tax does not match.'
        )

        # click finish
        self.place_order_page_instance.finish_overview()
        # validate success message
        assert (
            self.place_order_page_instance.get_checkout_status_message(),
            'Checkout: Complete!',
            'Status message incorrect.'
        )

        assert (
            self.place_order_page_instance.get_checkout_complete_message(),
            'Thank you for your order!',
            'Thank message incorrect.'
        )

    def tearDown(self) -> None:
        self.driver.quit()