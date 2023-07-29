from playwright.sync_api import Page, expect


class MenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.open_button = self.page.get_by_role("button", name="Open Menu")
        self.all_items_menu_item = self.page.get_by_role("link", name="All Items")
        self.about_menu_item = self.page.get_by_role("link", name="About")
        self.logout_menu_item = self.page.get_by_role("link", name="Logout")
        self.reset_menu_item = self.page.get_by_role("link", name="Reset App State")

    def logout(self):
        self.open_button.click()
        self.logout_menu_item.click()

    def open_menu(self):
        self.open_button.click()

    def reset_app_state(self):
        self.reset_menu_item.click()

    def open_all_items(self):
        self.all_items_menu_item.click()
