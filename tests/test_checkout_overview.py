from playwright.sync_api import expect


def test_check_prices_count(auth_clear):
    auth_clear.product_page.add_item_to_cart(0)
    auth_clear.product_page.add_item_to_cart(1)
    auth_clear.product_page.add_item_to_cart(2)
    auth_clear.product_page.open_shopping_cart()
    auth_clear.cart_page.cart_checkout()
    auth_clear.checkout_page.fill_checkout("John", "Doe", "012345")
    expect(auth_clear.get_title()).to_have_text("Checkout: Overview")

    cart_prices = auth_clear.checkout_overview.get_checkout_items_prices()
    subtotal_count = sum(cart_prices)
    tax_count = round(subtotal_count * 0.08, 2)
    total_count = subtotal_count + tax_count

    assert auth_clear.checkout_overview.get_subtotal() == subtotal_count
    assert auth_clear.checkout_overview.get_tax() == tax_count
    assert auth_clear.checkout_overview.get_total() == total_count
