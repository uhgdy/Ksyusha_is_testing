import pytest
from playwright.sync_api import Playwright


def buf(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return page


@pytest.fixture()
def fix(playwright: Playwright):
    return buf(playwright)


def test(fix):
    assert True
