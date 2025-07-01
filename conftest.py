# conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # fixed import
from Utilities.config_reader import get_base_url
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(
    filename="Logs\test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.fixture(scope="function")
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Recommended for Windows
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")  # For Linux environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Avoids shared memory issues in Docker/Linux
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.get(get_base_url())
    logging.info(f"Opened browser and navigated to {get_base_url()}")
    yield driver
    driver.quit()
