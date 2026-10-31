from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRM_MSG = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK)).click()

    def open_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

    def start_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()

    def fill_details(self, first, last, postal):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL).send_keys(postal)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def get_confirmation(self):
        return self.wait.until(EC.visibility_of_element_located(self.CONFIRM_MSG)).text