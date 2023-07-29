from playwright.sync_api import expect
import pytest


def test_open_products(auth_app):
    expect(auth_app.get_title()).to_contain_text("Products")
    expect(auth_app.product_page.get_product_list()).to_have_count(6)
    print(auth_app.product_page.get_product_list_prices())


cases = [("lohi", False), ("hilo", True)]
ids = ["Sort Low to High", "Sort High to Low"]


@pytest.mark.parametrize("sorting, reverse", cases, ids=ids)
def test_filter_products(auth_app, sorting, reverse):
    prices = [29.99, 9.99, 15.99, 49.99, 7.99, 15.99]
    auth_app.product_page.sort_products(sorting)
    assert auth_app.product_page.get_product_list_prices() == sorted(prices, reverse=reverse)


def test_add_item_to_cart(auth_app):
    auth_app.product_page.add_item_to_cart(0)
    expect(auth_app.product_page.get_cart_counter()).to_have_text("1")
    auth_app.product_page.add_item_to_cart(1)
    expect(auth_app.product_page.get_cart_counter()).to_have_text("2")
    auth_app.product_page.add_item_to_cart(2)
    expect(auth_app.product_page.get_cart_counter()).to_have_text("3")
    auth_app.product_page.remove_item_from_cart(2)
    expect(auth_app.product_page.get_cart_counter()).to_have_text("2")
    auth_app.product_page.remove_item_from_cart(1)
    expect(auth_app.product_page.get_cart_counter()).to_have_text("1")
    auth_app.product_page.remove_item_from_cart(0)
    expect(auth_app.product_page.get_cart_counter()).not_to_be_visible()
