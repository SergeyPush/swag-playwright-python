from playwright.sync_api import expect
import pytest


def test_fill_checkout(auth_clear):
    auth_clear.product_page.add_item_to_cart(0)
    auth_clear.product_page.add_item_to_cart(1)
    auth_clear.product_page.open_shopping_cart()
    auth_clear.cart_page.cart_checkout()
    auth_clear.checkout_page.fill_checkout("John", "Doe", "012345")
    assert auth_clear.get_title().inner_text() == "Checkout: Overview"


cases = [
    ("", "", "", "Error: First Name is required"),
    ("John", "", "123456", "Error: Last Name is required"),
    ("John", "Doe", "", "Error: Postal Code is required"),
    ("", "Doe", "123456", "Error: First Name is required"),
    ("", "", "123456", "Error: First Name is required")
]
ids = ["All fields are empty", "Last name is empty", "Postal code is empty", "First name is empty",
       "First and last name are empty"]


@pytest.mark.parametrize("first_name, last_name, postal_code, expected", cases, ids=ids)
def test_fill_checkout_incorrect_data(auth_clear, first_name, last_name, postal_code, expected):
    auth_clear.product_page.add_item_to_cart(0)
    auth_clear.product_page.open_shopping_cart()
    auth_clear.cart_page.cart_checkout()
    auth_clear.checkout_page.fill_checkout(first_name, last_name, postal_code)
    expect(auth_clear.checkout_page.error_message).to_have_text(expected)


def test_cancel_checkout(auth_clear):
    auth_clear.product_page.add_item_to_cart(0)
    auth_clear.product_page.open_shopping_cart()
    auth_clear.cart_page.cart_checkout()
    assert auth_clear.get_title().inner_text() == "Checkout: Your Information"
    auth_clear.checkout_page.cancel_checkout()
    assert auth_clear.get_title().inner_text() == "Your Cart"
    expect(auth_clear.get_title()).to_have_text("Your Cart")
