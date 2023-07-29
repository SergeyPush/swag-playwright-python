from playwright.sync_api import Page


class CheckoutCompletePage:
    def __init__(self, page: Page):
        self._page = page
        self.complete_label = self._page.locator("h2.complete-header")
        self.back_button = self._page.locator("text=Back Home")
        self.complete_text_label = self._page.locator(".complete-text")

    def get_complete_label(self):
        return self.complete_label

    def get_complete_text_label(self):
        return self.complete_text_label

    def click_back_button(self):
        self.back_button.click()
