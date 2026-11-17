from playwright.sync_api import Page, expect
from login_helper import login

def test_login(page: Page):
    login(page)
    expect(page.locator(".inventory_container")).to_be_visible()


def test_wrong_password_login(page: Page):
    login(page, password="secret_sauce2")
    expect(page.locator(".error_icon")).to_have_count(2)
    expect(page.locator(".error-message-container")).to_be_visible()
    expect(page.locator(".error-message-container")).to_contain_text("do not match")


def test_locked_out_user(page: Page):
    login(page, "locked_out_user")
    expect(page.locator(".error-message-container")).to_be_visible()
    expect(page.locator(".error-message-container")).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page.locator(".error-message-container")).to_have_css("background-color", "rgb(226, 35, 26)")
    expect(page.locator(".error-message-container h3")).to_have_css("color", "rgb(255, 255, 255)")
    expect(page.get_by_role("alert")).to_have_css("color", "rgb(255, 255, 255)")

