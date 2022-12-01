import pytest
from playwright.sync_api import Playwright


# создание страницы
@pytest.fixture()
def creating_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return page


# авторизация
@pytest.fixture()
def authorization(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/")
    page.get_by_role("button", name="Вход").click()
    page.frame_locator("#root iframe").locator("#phone-or-email-login").click()
    page.frame_locator("#root iframe").locator("#phone-or-email-login").fill("uhgdy_1@mail.ru")
    page.frame_locator("#root iframe").frame_locator("[data-testid=\"checkbox-iframe\"]").get_by_role("checkbox",
                                                                                                      name="SmartCaptcha нужна проверка пользователя").click()
    page.frame_locator("#root iframe").get_by_role("button", name="Продолжить").click()
    page.frame_locator("#root iframe").locator("#login-password").fill("qqqqq1")
    page.frame_locator("#root iframe").locator("#login-password").press("Enter")
    yield page
