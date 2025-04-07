from selenium.webdriver.common.by import By

from pages.basePage import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'oxd-alert')]")

    def login(self, username, password):
        self.enter_text(*self.USERNAME_INPUT, text=username)
        self.enter_text(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.wait_for_element(*self.ERROR_MESSAGE).text