# pages/base_page.py
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        logging.info(f"Clicking on element: {by_locator}")
        self.driver.find_element(*by_locator).click()

    def enter_text(self, by_locator, value):
        logging.info(f"Entering text: '{value}' in {by_locator}")
        self.driver.find_element(*by_locator).send_keys(value)

    def get_text(self, by_locator):
        text = self.driver.find_element(*by_locator).text
        logging.info(f"Text at {by_locator}: {text}")
        return text

    def is_visible(self, by_locator):
        visible = self.driver.find_element(*by_locator).is_displayed()
        logging.info(f"Element visibility for {by_locator}: {visible}")
        return visible
