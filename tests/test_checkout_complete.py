from playwright.sync_api import expect


def test_check_finish_page(auth_clear):
    auth_clear.product_page.add_item_to_cart(0)
    auth_clear.product_page.open_shopping_cart()
    auth_clear.cart_page.cart_checkout()
    auth_clear.checkout_page.fill_checkout("John", "Doe", "012345")
    expect(auth_clear.get_title()).to_have_text("Checkout: Overview")
    auth_clear.checkout_overview.click_finish_button()
    expect(auth_clear.get_title()).to_have_text("Checkout: Complete!")
    expect(auth_clear.checkout_complete.get_complete_label()).to_have_text("Thank you for your order!")
    expect(auth_clear.checkout_complete.get_complete_text_label()).to_have_text(
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!")


def test_check_back_home(auth_clear):
    auth_clear.product_page.add_item_to_cart(0)
    auth_clear.product_page.open_shopping_cart()
    auth_clear.cart_page.cart_checkout()
    auth_clear.checkout_page.fill_checkout("John", "Doe", "012345")
    expect(auth_clear.get_title()).to_have_text("Checkout: Overview")
    auth_clear.checkout_overview.click_finish_button()
    auth_clear.checkout_complete.click_back_button()
    expect(auth_clear.get_title()).to_have_text("Products")
