import allure
from playwright.sync_api import Page, expect


class AuthPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.welcome_title = page.get_by_text("Welcome", exact=True)
        self.welcome_farsi = page.get_by_text("خوش آمدید")
        self.name_input = page.get_by_placeholder("e.g. Sara")
        self.name_input_farsi = page.get_by_placeholder("مثلاً سارا")
        self.create_account_button = page.get_by_role("button", name="Create Account")
        self.login_switch_link = page.get_by_text("Already have an account? Log in", exact=True)
        self.login_button = page.get_by_role("button", name="Log in")

    @allure.step("Open application")
    def open(self):
        self.page.goto(self.base_url)

    @allure.step("Verify auth screen is visible")
    def should_be_visible(self):
        title_visible = self.welcome_title.is_visible()
        farsi_visible = self.welcome_farsi.is_visible()
        assert title_visible+farsi_visible == 1
        if title_visible:
            expect(self.name_input).to_be_visible()
        if farsi_visible:
            expect(self.name_input_farsi).to_be_visible()

    @allure.step("Create account for user: {username}")
    def create_account(self, username: str):
        self.name_input.fill(username)
        self.create_account_button.click()

    @allure.step("Switch to login mode")
    def switch_to_login(self):
        self.login_switch_link.click()
        expect(self.login_button).to_be_visible()

    @allure.step("Login with user: {username}")
    def login(self, username: str):
        self.switch_to_login()
        self.name_input.fill(username)
        self.login_button.click()
