from playwright.sync_api import expect


def test_open_shopping_cart(auth_clear):
    auth_clear.product_page.open_shopping_cart()
    assert auth_clear.get_title().inner_text() == 'Your Cart'


def test_open_cart(auth_clear):
    auth_clear.product_page.open_shopping_cart()
    assert auth_clear.get_title().inner_text() == "Your Cart"
    auth_clear.cart_page.back_to_products()
    assert auth_clear.get_title().inner_text() == "Products"


def test_check_products_added_to_cart(auth_clear):
    product1 = auth_clear.product_page.add_item_to_cart(0)
    product2 = auth_clear.product_page.add_item_to_cart(1)
    auth_clear.product_page.open_shopping_cart()
    expect(auth_clear.cart_page.get_cart_items()).to_have_count(2)
    expect(auth_clear.cart_page.get_cart_item_names()).to_have_text([product1, product2])


def test_open_checkout(auth_clear):
    auth_clear.product_page.add_item_to_cart(0)
    auth_clear.product_page.add_item_to_cart(1)
    auth_clear.product_page.open_shopping_cart()
    expect(auth_clear.cart_page.get_cart_items()).to_have_count(2)
    auth_clear.cart_page.cart_checkout()
    assert auth_clear.get_title().inner_text() == "Checkout: Your Information"
