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


@allure.title("Game screen should load for user nima")
@pytest.mark.p0
def test_game_screen_loaded(page):
    prepare_logged_in_user(page)
    game_page = GamePage(page)
    game_page.should_be_visible_for_user(DEFAULT_USER)
    game_page.should_have_empty_board()


@allure.title("User nima can make one valid move")
@pytest.mark.p0
def test_user_can_make_a_move(page):
    prepare_logged_in_user(page)
    game_page = GamePage(page)
    game_page.play_move(0)
    game_page.should_cell_contain_valid_mark(0)
