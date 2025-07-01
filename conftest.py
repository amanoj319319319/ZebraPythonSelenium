# conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # fixed import
from Utilities.config_reader import get_base_url
import logging

logging.basicConfig(
    filename="Logs/test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.get(get_base_url())
    logging.info(f"Opened browser and navigated to {get_base_url()}")
    yield driver
    driver.quit()
