import pytest
from pages.loginPage import LoginPage
from utils.test_data import login_credentials
import time

@pytest.mark.parametrize("username,password,expected", login_credentials)
def test_login(driver, username, password, expected):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    time.sleep(2)

    if expected:
        assert "dashboard" in driver.current_url.lower()
    else:
        error_text = login_page.get_error_message()
        assert "Invalid credentials" in error_text