from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.back_button = self.page.locator("text=Continue Shopping")
        self.cart_items = self.page.locator(".cart_item")
        self.checkout_button = self.page.get_by_role("button", name="Checkout")

    def back_to_products(self):
        self.back_button.click()

    def get_cart_items(self):
        return self.cart_items

    def get_cart_item_names(self):
        return self.get_cart_items().locator(".inventory_item_name")

    def remove_item_from_cart(self, id):
        item = self.get_cart_items().nth(id)
        item.locator("text=Remove").click()
        return item.locator(".inventory_item_name")

    def cart_checkout(self):
        self.checkout_button.click()
