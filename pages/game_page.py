import allure
from playwright.sync_api import Page, expect


class GamePage:
    def __init__(self, page: Page):
        self.page = page
        self.play_tab = page.get_by_role("button", name="Play")
        self.profile_tab = page.get_by_role("button", name="Profile")
        self.history_tab = page.get_by_role("button", name="History")
        self.logout_button = page.get_by_role("button", name="Log Out")
        self.new_game_button = page.get_by_role("button", name="New Game")
        self.hint_button = page.get_by_role("button", name="Get Hint")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.status = page.get_by_text("Your turn (X)", exact=True)

    def greeting(self, username: str):
        return self.page.get_by_text(f"Hello, {username}", exact=True)

    def cell(self, index: int):
        return self.page.locator(f'[data-testid="cell-{index}"]')

    @allure.step("Verify game screen is visible for user: {username}")
    def should_be_visible_for_user(self, username: str):
        expect(self.greeting(username)).to_be_visible()
        expect(self.play_tab).to_be_visible()
        expect(self.profile_tab).to_be_visible()
        expect(self.history_tab).to_be_visible()
        expect(self.logout_button).to_be_visible()
        expect(self.status).to_be_visible()

    @allure.step("Verify the board is empty")
    def should_have_empty_board(self):
        for i in range(9):
            expect(self.cell(i)).to_be_visible()
            expect(self.cell(i)).to_have_text("")

    @allure.step("Play move on cell index: {index}")
    def play_move(self, index: int):
        expect(self.cell(index)).to_be_visible()
        self.cell(index).click()

    @allure.step("Verify cell contains a valid mark at index: {index}")
    def should_cell_contain_valid_mark(self, index: int):
        text = self.cell(index).inner_text().strip()
        assert text in {"X", "O"}

    @allure.step("Click New Game")
    def click_new_game(self):
        self.new_game_button.click()

    @allure.step("Click Get Hint")
    def click_hint(self):
        self.hint_button.click()

    @allure.step("Click Reset")
    def click_reset(self):
        self.reset_button.click()

    @allure.step("Log out from the application")
    def logout(self):
        self.logout_button.click()
