import allure
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:8000/index.html"
DEFAULT_USER = "nima"


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture()
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture()
def context(browser):
    context = browser.new_context(viewport={"width": 1365, "height": 900})
    yield context
    context.close()


@pytest.fixture()
def page(context):
    page = context.new_page()
    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            results_dir = Path("allure-results")
            results_dir.mkdir(exist_ok=True)
            screenshot_path = results_dir / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            allure.attach.file(str(screenshot_path), name=item.name, attachment_type=allure.attachment_type.PNG)
