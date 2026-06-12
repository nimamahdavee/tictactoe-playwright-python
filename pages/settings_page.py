import allure
from playwright.sync_api import Page


class SettingsPage:
    def __init__(self, page: Page):
        self.page = page
        self.language_select = page.locator('select').first
        self.theme_button = page.get_by_role('button', name='Dark')

    @allure.step("Change language")
    def change_language(self):
        current = self.language_select.input_value()
        target = 'fa' if current == 'en' else 'en'
        self.language_select.select_option(target)

    @allure.step("Toggle theme")
    def toggle_theme(self):
        self.theme_button.click()
