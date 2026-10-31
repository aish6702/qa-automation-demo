import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

@pytest.mark.parametrize("user, pwd, expected", [
    ("standard_user", "wrong123", "do not match"),
    ("locked_out_user", "secret_sauce", "locked out"),
    ("", "", "Username is required"),
])
def test_invalid_login(driver, user, pwd, expected):
    page = LoginPage(driver)
    page.open()
    page.login(user, pwd)
    assert expected in page.get_error()