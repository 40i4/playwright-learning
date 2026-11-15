from playwright.sync_api import Page

def login(page: Page, username: str = "standard_user", password: str = "secret_sauce") -> None:
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")