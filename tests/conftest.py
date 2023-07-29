from playwright.sync_api import Playwright, sync_playwright, expect
from pytest import fixture

from page_objects.app import Application


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session', params=["chromium"], ids=["chromium"])
def get_browser(get_playwright, request):
    browser = request.param
    headless = True
    slow_mo = None
    browser_instance = get_playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
    # match browser:
    #     case "chromium":
    #
    #     case "firefox":
    #         browser_instance = get_playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
    #     case "chrome":
    #         browser_instance = get_playwright.webkit.launch(headless=headless, slow_mo=slow_mo)
    yield browser_instance
    browser_instance.close()


@fixture(scope='module')
def app(get_browser):
    context = get_browser.new_context()
    page = context.new_page()
    app = Application(page)
    app.open_app()
    app.page.wait_for_load_state()
    yield app
    app.page.close()


@fixture(scope="module")
def auth_app(app):
    app.login_page.standard_user_login()
    app.page.context.storage_state()
    yield app
    app.page.close()


@fixture(scope="function")
def auth_clear(auth_app):
    yield auth_app
    auth_app.clear_state()
