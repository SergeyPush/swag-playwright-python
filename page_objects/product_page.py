from playwright.sync_api import Page, expect


class ProductPage():
    def __init__(self, page: Page):
        self.page = page
        self.product_list = page.locator('.inventory_item')
        self.filter_dropdown = page.locator("[data-test=\"product_sort_container\"]")
        self.cart_counter = page.locator(".shopping_cart_badge")
        self.shopping_cart_button = page.locator("a.shopping_cart_link")

    def get_product_list(self):
        return self.product_list

    def get_product_list_prices(self):
        prices = self.get_product_list().locator(".inventory_item_price").all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def sort_products(self, option):
        self.filter_dropdown.select_option(option)

    def get_cart_counter(self):
        return self.cart_counter

    def add_item_to_cart(self, id):
        button = self.product_list.nth(id).get_by_text("Add to cart")
        button.click()
        expect(button).not_to_be_visible()
        return self.product_list.nth(id).locator(".inventory_item_name").inner_text()

    def remove_item_from_cart(self, id):
        button = self.product_list.nth(id).get_by_text("Remove")
        button.click()
        expect(button).not_to_be_visible()

    def open_shopping_cart(self):
        self.shopping_cart_button.click()
        self.page.wait_for_load_state()
