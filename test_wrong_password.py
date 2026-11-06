from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce2")
    page.click("#login-button")
    expect(page.locator(".error_icon")).to_have_count(2)
    expect(page.locator(".error-message-container")).to_be_visible()
    expect(page.locator(".error-message-container")).to_contain_text("do not match")