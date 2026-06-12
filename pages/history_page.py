import allure
from playwright.sync_api import Page, expect


class HistoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.get_by_role("heading", name="History")

    @allure.step("Verify history screen is visible")
    def should_be_visible(self):
        expect(self.title).to_be_visible()
