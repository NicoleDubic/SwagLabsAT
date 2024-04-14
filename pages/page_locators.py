from selenium.webdriver.common.by import By


class LoginPageData:
    # salvam toate datele necesare testarii paginii de login
    log_in_page_url = "https://www.saucedemo.com/"
    successfully_logged_in_url = "https://www.saucedemo.com/inventory.html"
    successfully_logged_in_text = "Products"
    username_password_invalid_expected_message = "Epic sadface: Username and password do not match any user in this service"
    standard_user = "standard_user"
    locked_out_user = "locked_out_user"
    problem_user = "problem_user"
    performance_glitch_user = "performance_glitch_user"
    error_user = "error_user"
    visual_user = "visual_user"
    users_password = "secret_sauce"
    invalid_username = "alan"
    invalid_password = "pass123"
    login_page_title = "Swag Labs"

class LoginPageLocators:
    # salvam toate obiectele din pagina de login
    username_field_xpath = (By.XPATH, "//input[@id='user-name']")
    password_field_by_id = (By.ID, "password")
    password_field_xpath = (By.XPATH, "//input[@id='password']")
    submit_field_xpath = (By.XPATH, "//*[@id='login-button']")
    logged_in_successfully_xpath = (By.XPATH, "//h1[@class='title']")
    logged_in_failed_xpath = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
    burger_menu_button = (By.ID, "react-burger-menu-btn")
    log_out_button_link = (By.LINK_TEXT, "Logout")



class InventoryPageLocators:
    items_titles = "inventory_item_name"
    items_prices = "inventory_item_price"
    inventory_item_button = "//div[@class='inventory_item']//button"
    select_product_sort_container = "//*[@id='header_container']/div[2]/div/span/select"
    get_product_sort_container = (By.XPATH, "//select[@data-test='product_sort_container']")
    burger_item_button = LoginPageLocators.burger_menu_button
    sidebar_button = "reset_sidebar_link"
    burger_cross_button = "react-burger-cross-btn"
    shopping_cart_button = "shopping_cart_link"
    checkout_button = "//button[@id='checkout']"
    inventory_item_name = "inventory_item_name"
    inventory_item_price = "inventory_item_price"

class PlaceOrderPageData:
    first_name = "John"
    last_name = "State"
    zip_postal_code = "006196"

class PlaceOrderPageLocators:
    first_name_field = "first-name"
    last_name_field = "last-name"
    zip_postal_code_field = "postal-code"
    continue_button = "continue"
    summary_subtotal_label = "summary_subtotal_label"
    finish_button = "finish"
    status_message = "title"
    complete_message = "complete-header"