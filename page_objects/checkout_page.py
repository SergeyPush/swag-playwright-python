from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = self.page.locator("[data-test=\"firstName\"]")
        self.last_name_input = self.page.locator("[data-test=\"lastName\"]")
        self.postal_code_input = self.page.locator("[data-test=\"postalCode\"]")
        self.cancel_button = self.page.get_by_role("button", name="cancel")
        self.continue_button = self.page.get_by_role("button", name="continue")
        self.error_message = self.page.locator(".error-message-container h3")
        self.error_circles = self.page.locator("[data-icon=\"times-circle\"]")

    def fill_checkout(self, first_name="John", last_name="Doe", postal_code="012345"):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()

    def get_error_message(self):
        expect(self.error_circles).to_be_visible()
        return self.error_message()
