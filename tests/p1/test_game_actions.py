import allure
import pytest
from pages.auth_page import AuthPage
from pages.game_page import GamePage
from tests.conftest import BASE_URL, DEFAULT_USER


def prepare_logged_in_user(page):
    auth_page = AuthPage(page, BASE_URL)
    auth_page.open()
    auth_page.should_be_visible()
    auth_page.create_account(DEFAULT_USER)


@allure.title("New Game resets the board")
@pytest.mark.p1
def test_new_game_button(page):
    prepare_logged_in_user(page)
    game_page = GamePage(page)
    game_page.play_move(0)
    game_page.click_new_game()
    game_page.should_have_empty_board()


@allure.title("Hint action works without breaking the page")
@pytest.mark.p1
def test_hint_button(page):
    prepare_logged_in_user(page)
    game_page = GamePage(page)
    game_page.click_hint()
    game_page.should_be_visible_for_user(DEFAULT_USER)


@allure.title("Reset clears the board")
@pytest.mark.p1
def test_reset_button(page):
    prepare_logged_in_user(page)
    game_page = GamePage(page)
    game_page.play_move(0)
    game_page.click_reset()
    game_page.should_have_empty_board()
