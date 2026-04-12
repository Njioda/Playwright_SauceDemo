from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.inventory_page import InventoryPage


def test_login_and_inventory_validation(page):
    

        login_page = LoginPage(page)
        # Open page
        login_page.navigate()

        # Login
        login_page.login("standard_user", "secret_sauce")
        
        # Warten bis Navigation fertig
        page.wait_for_url("**/inventory.html")

        # Jetzt prüfen
        login_page.wait_until_loaded()
        assert login_page.is_loaded()