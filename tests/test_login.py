from playwright.sync_api import expect
import pytest


def test_login_success(app):
    app.login_page.login("standard_user", "secret_sauce")
    expect(app.get_title()).to_contain_text("Products")
    app.menu_page.logout()


def test_logout_success(app):
    app.login_page.login("standard_user", "secret_sauce")
    app.menu_page.logout()
    expect(app.login_page.accepted_usernames_list).to_be_visible()


cases = [
    ("username", "password", "Epic sadface: Username and password do not match any user in this service"),
    ("username", "", "Epic sadface: Password is required"),
    ("", "password", "Epic sadface: Username is required"),
    ("", "", "Epic sadface: Username is required")
]
ids = ["Incorrect credentials", "Empty password", "Empty username", "Empty credentials"]


@pytest.mark.parametrize('username, password, expected', cases, ids=ids)
def test_login_fail(app, username, password, expected):
    app.login_page.login(username, password)
    expect(app.login_page.error_message).to_be_visible()
    expect(app.login_page.input_error_label).to_have_count(2)
    expect(app.login_page.error_message).to_contain_text(expected)
