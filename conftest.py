import pytest
from playwright.sync_api import Playwright


# создание страницы
@pytest.fixture()
def creating_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return page


# авторизация ru
@pytest.fixture()
def authorization_ru(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/")
    page.get_by_role("button", name="Хорошо, продолжим").click()
    page.get_by_role("button", name="Вход").click()
    page.frame_locator("#root iframe >> nth=0").locator("#phone-or-email-login").click()
    page.frame_locator("#root iframe >> nth=0").locator("#phone-or-email-login").fill("uhgdy_1@mail.ru")
    page.frame_locator("#root iframe >> nth=0").frame_locator("[data-testid=\"checkbox-iframe\"]").get_by_role("checkbox", name="SmartCaptcha нужна проверка пользователя").click()
    page.frame_locator("#root iframe >> nth=0").get_by_role("button", name="Продолжить").click()
    page.frame_locator("#root iframe >> nth=0").locator("#login-password").fill("qqqqq1")
    page.frame_locator("#root iframe >> nth=0").get_by_role("button", name="Войти").click()

    yield page


# авторизация dev
@pytest.fixture()
def authorization_dev(creating_page):
    page = creating_page
    page.goto("https://rutube.dev/")
    page.get_by_role("button", name="Хорошо, продолжим").click()
    page.get_by_role("button", name="Вход").click()
    page.frame_locator("#root iframe >> nth=0").locator("#phone-or-email-login").click()
    page.frame_locator("#root iframe >> nth=0").locator("#phone-or-email-login").fill("uhgdy_1@mail.ru")
    page.frame_locator("#root iframe >> nth=0").get_by_role("button", name="Продолжить").click()
    page.frame_locator("#root iframe >> nth=0").locator("#login-password").fill("111111")
    page.frame_locator("#root iframe >> nth=0").get_by_role("button", name="Войти").click()

    yield page