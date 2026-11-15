from playwright.sync_api import Page, expect
from login_helper import login

def test_login(page: Page):
    login(page, "standard_user", "secret_sauce2")
    expect(page.locator(".error_icon")).to_have_count(2)
    expect(page.locator(".error-message-container")).to_be_visible()
    expect(page.locator(".error-message-container")).to_contain_text("do not match")