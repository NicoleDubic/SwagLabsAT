from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):
        self.driver = driver

#Login Page
    def open_url(self, url: str):
        self.driver.get(url)

        # get current url
    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

        # finds an element and returns it
    def find(self, locator: tuple):  # tuple (By.XPATH, "//element")
        return self.driver.find_element(*locator)

    # wait for an element to appear on the page
    def wait_for_visibile_element(self, locator: tuple, time=5):
        ex_wait = WebDriverWait(self.driver, time)
        ex_wait.until(EC.visibility_of_element_located(locator))

    # wait for an element to appear on the page
    def wait_for_clickable_element(self, locator: tuple):
        wait = WebDriverWait(self.driver, 4)
        wait.until(EC.element_to_be_clickable(locator))

    # type text in a input label element
    def type_text(self, input_label, message: str):
        self.wait_for_visibile_element(input_label, 7)
        self.find(input_label).send_keys(message)

    # get text from a label
    def get_text(self, label: tuple):
        self.wait_for_visibile_element(label)
        return self.find(label).text

    # is the object displayed
    def is_object_displayed(self, element):
        try:
            return self.find(element).is_displayed()
        except NoSuchElementException:
            return False

    # click the button
    def click(self, button: tuple):
        self.wait_for_clickable_element(button)
        self.find(button).click()

#Inventory Page
    def get_items_titles(self, class_locator: tuple):
        items_titles = []
        for item_title in self.driver.find_elements(By.CLASS_NAME, class_locator):
            items_titles.append(item_title.text)
        return items_titles


    def get_items_prices(self, class_locator):
        items_prices = []
        for item_price in self.driver.find_elements(By.CLASS_NAME, class_locator):
            only_numbers = item_price.text.replace('$', '')
            items_prices.append(float(only_numbers))
        return items_prices


    def get_buttons_list_by_xpath(self, xpath_locator):
        return self.driver.find_elements(By.XPATH, xpath_locator)


    def select_by_visible_text(self, xpath_locator, visible_text):
        select = Select(self.driver.find_element(By.XPATH, xpath_locator))
        select.select_by_visible_text(visible_text)


    def get_visible_text_selected(self, xpath_locator):
        select = Select(self.driver.find_element(By.XPATH, xpath_locator))
        return select.first_selected_option.text

    def click_element_by_id(self, id_locator):
        element_to_be_clicked = self.driver.find_element(By.ID, id_locator)
        wait = WebDriverWait(self.driver, 4)
        wait.until(EC.element_to_be_clickable(element_to_be_clicked))
        element_to_be_clicked.click()



    def click_element_by_class(self, class_locator):
        self.driver.find_element(By.CLASS_NAME, class_locator).click()

    def click_element_by_xpath(self, xpath_locator):
        self.driver.find_element(By.XPATH, xpath_locator).click()

#Place order page
    def insert_text_by_id(self, id_locator, text):
        self.driver.find_element(By.ID, id_locator).send_keys(text)

    def get_text_by_class(self, class_locator):
        return self.driver.find_element(By.CLASS_NAME, class_locator).text