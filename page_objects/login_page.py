from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = self.page.locator("[data-test=\"username\"]")
        self.password = self.page.locator("[data-test=\"password\"]")
        self.loginButton = self.page.locator("[data-test=\"login-button\"]")
        self.accepted_usernames_list = self.page.locator("#root div").filter(
            has_text="Accepted usernames are:standard_userlocked_out_userproblem_userperformance_glitc").nth(3)
        self.error_message = self.page.locator(".error-message-container")
        self.input_error_label = page.locator("css=.input_error")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginButton.click()

    def get_error(self):
        return self.error_message

    def standard_user_login(self):
        self.login("standard_user", "secret_sauce")
