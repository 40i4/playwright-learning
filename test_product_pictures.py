from playwright.sync_api import Page, expect
from login_helper import login

def test_product_pictures(page: Page):
    backpack_image = page.get_by_alt_text("Sauce Labs Backpack")
    bike_light_image = page.get_by_alt_text("Sauce Labs Bike Light")
    bolt_tshirt_image = page.get_by_alt_text("Sauce Labs Bolt T-Shirt")
    fleece_jacket_image = page.get_by_alt_text("Sauce Labs Fleece Jacket")
    onesie_image = page.get_by_alt_text("Sauce Labs Onesie")
    test_allthethings_tshirt_image = page.get_by_alt_text("Test.allTheThings() T-Shirt (Red)")
    
    login(page)

    expect(backpack_image).to_have_attribute("src", "/assets/sauce-backpack-1200x1500-CjRW-Djj.jpg")
    expect(bike_light_image).to_have_attribute("src", "/assets/bike-light-1200x1500-DxcZRFOA.jpg")
    expect(bolt_tshirt_image).to_have_attribute("src", "/assets/bolt-shirt-1200x1500-mR0ldpVS.jpg")
    expect(fleece_jacket_image).to_have_attribute("src", "/assets/sauce-pullover-1200x1500-BfbI-PSd.jpg")
    expect(onesie_image).to_have_attribute("src", "/assets/red-onesie-1200x1500-BrSuq0ic.jpg")
    expect(test_allthethings_tshirt_image).to_have_attribute("src", "/assets/red-tatt-1200x1500-E-qp6aYf.jpg")