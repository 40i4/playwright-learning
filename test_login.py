from playwright.sync_api import Page, expect
from login_helper import login

def test_login(page: Page):
    login(page)
    expect(page.locator(".inventory_container")).to_be_visible()
