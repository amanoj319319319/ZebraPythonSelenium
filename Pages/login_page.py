# pages/login_page.py

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
import logging

class LoginPage(BasePage):
    # Locators for login elements
    USERNAME_INPUT = (By.ID, "email")      # Adjust IDs/selectors as per actual app
    PASSWORD_INPUT = (By.ID, "login-password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.ID, "incorrectdetails")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        logging.info("LoginPage initialized")

    def login(self, username, password):
        logging.info(f"Attempting login with username: {username}")
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
