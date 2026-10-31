from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

def test_full_checkout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    c = CheckoutPage(driver)
    c.add_backpack()
    c.open_cart()
    c.start_checkout()
    c.fill_details("Aish", "Ayub", "46000")
    c.finish()

    assert "Thank you for your order" in c.get_confirmation()