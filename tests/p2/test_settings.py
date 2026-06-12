import allure
import pytest
from pages.auth_page import AuthPage
from pages.settings_page import SettingsPage
from tests.conftest import BASE_URL


@allure.title("Language can be changed")
@pytest.mark.p2
def test_change_language(page):
    auth_page = AuthPage(page, BASE_URL)
    settings_page = SettingsPage(page)
    auth_page.open()
    auth_page.should_be_visible()
    settings_page.change_language()
    auth_page.should_be_visible()


@allure.title("Theme can be toggled")
@pytest.mark.p2
def test_toggle_theme(page):
    auth_page = AuthPage(page, BASE_URL)
    settings_page = SettingsPage(page)
    auth_page.open()
    auth_page.should_be_visible()
    settings_page.toggle_theme()
    auth_page.should_be_visible()
