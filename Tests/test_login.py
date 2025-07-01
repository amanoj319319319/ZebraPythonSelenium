# tests/test_login.py
import pytest
import time
from Pages.login_page import LoginPage
from Utilities.config_reader import get_valid_credentials, get_invalid_credentials

@pytest.mark.testrail_case_id(1)
def test_valid_login(setup):
    username, password = get_valid_credentials()
    login_page = LoginPage(setup)
    login_page.login(username, password)
    time.sleep(5)
    assert "My Courses" in setup.title

@pytest.mark.testrail_case_id(2)
def test_invalid_login(setup):
    username, password = get_invalid_credentials()
    login_page = LoginPage(setup)
    login_page.login(username, password)
    time.sleep(5)
    assert "Incorrect login details" in login_page.get_error_message()
