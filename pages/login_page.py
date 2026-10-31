from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, user, pwd):
        self.driver.find_element(*self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_error(self):
        return self.driver.find_element(*self.ERROR).text