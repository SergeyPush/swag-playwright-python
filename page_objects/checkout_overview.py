from playwright.sync_api import Page


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self._page = page
        self.checkout_items = self._page.locator(".cart_item")
        self.cancel_button = self._page.get_by_role("button", name="cancel")
        self.finish_button = self._page.get_by_role("button", name="finish")
        self.subtotal_label = self._page.locator(".summary_subtotal_label")
        self.tax_label = self._page.locator(".summary_tax_label")
        self.total_label = self._page.locator(".summary_total_label")

    def get_checkout_items(self):
        return self.checkout_items

    def get_checkout_items_prices(self):
        return self._get_prices(self.checkout_items.locator(".inventory_item_price").all_inner_texts())

    def get_subtotal(self):
        return self._get_prices(self.subtotal_label.inner_text())

    def get_tax(self):
        return self._get_prices(self.tax_label.inner_text())

    def get_total(self):
        return self._get_prices(self.total_label.inner_text())

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_finish_button(self):
        self.finish_button.click()

    def _get_prices(self, item: str | list):
        extract_number = lambda x: float(x.split("$")[1])
        if type(item) is list:
            return [extract_number(i) for i in item]
        return extract_number(item)
