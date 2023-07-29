from playwright.sync_api import Page, expect

from page_objects.cart_page import CartPage
from page_objects.checkout_complete import CheckoutCompletePage
from page_objects.checkout_overview import CheckoutOverviewPage
from page_objects.checkout_page import CheckoutPage
from page_objects.login_page import LoginPage
from page_objects.menu_page import MenuPage
from page_objects.product_page import ProductPage


class Application:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://www.saucedemo.com/'
        self.login_page = LoginPage(self.page)
        self.menu_page = MenuPage(self.page)
        self.product_page = ProductPage(self.page)
        self.cart_page = CartPage(self.page)
        self.checkout_page = CheckoutPage(self.page)
        self.checkout_overview = CheckoutOverviewPage(self.page)
        self.checkout_complete = CheckoutCompletePage(self.page)

    def open_app(self):
        self.page.goto(self.url)
        assert self.page.title() == 'Swag Labs'

    def get_title(self):
        return self.page.locator("css=.title")

    def clear_state(self):
        self.menu_page.open_menu()
        self.menu_page.reset_app_state()
        self.menu_page.open_all_items()
