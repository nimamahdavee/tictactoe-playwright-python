import allure
import pytest
from pages.auth_page import AuthPage
from pages.game_page import GamePage
from pages.profile_page import ProfilePage
from pages.history_page import HistoryPage
from tests.conftest import BASE_URL, DEFAULT_USER


def prepare_logged_in_user(page):
    auth_page = AuthPage(page, BASE_URL)
    auth_page.open()
    auth_page.should_be_visible()
    auth_page.create_account(DEFAULT_USER)


@allure.title("Profile tab can be opened")
@pytest.mark.p1
def test_open_profile(page):
    prepare_logged_in_user(page)
    game_page = GamePage(page)
    profile_page = ProfilePage(page)
    game_page.profile_tab.click()
    profile_page.should_be_visible()


@allure.title("History tab can be opened")
@pytest.mark.p1
def test_open_history(page):
    prepare_logged_in_user(page)
    game_page = GamePage(page)
    history_page = HistoryPage(page)
    game_page.history_tab.click()
    history_page.should_be_visible()
