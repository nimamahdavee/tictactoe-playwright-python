import allure
import pytest
from playwright.sync_api import expect
from pages.auth_page import AuthPage
from pages.game_page import GamePage
from tests.conftest import BASE_URL, DEFAULT_USER


@allure.title("Create account first with user nima")
@pytest.mark.p0
def test_create_account_with_nima(page):
    auth_page = AuthPage(page, BASE_URL)
    game_page = GamePage(page)

    auth_page.open()
    auth_page.should_be_visible()
    auth_page.create_account(DEFAULT_USER)
    game_page.should_be_visible_for_user(DEFAULT_USER)


@allure.title("Logout after successful account access")
@pytest.mark.p0
def test_logout_after_successful_access(page):
    auth_page = AuthPage(page, BASE_URL)
    game_page = GamePage(page)

    auth_page.open()
    auth_page.should_be_visible()
    auth_page.create_account(DEFAULT_USER)
    game_page.should_be_visible_for_user(DEFAULT_USER)
    game_page.logout()
    auth_page.should_be_visible()


@allure.title("Login with existing user nima")
@pytest.mark.p0
def test_login_with_existing_user_nima(page):
    auth_page = AuthPage(page, BASE_URL)
    game_page = GamePage(page)

    auth_page.open()
    auth_page.should_be_visible()
    auth_page.create_account(DEFAULT_USER)
    game_page.should_be_visible_for_user(DEFAULT_USER)
    game_page.logout()
    auth_page.should_be_visible()
    auth_page.login(DEFAULT_USER)
    game_page.should_be_visible_for_user(DEFAULT_USER)
    expect(page.get_by_text("Hello, nima", exact=True)).to_be_visible()
