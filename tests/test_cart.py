from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from playwright.sync_api import sync_playwright


def test_add_to_cart_and_verify(page):
    
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        # Wait for inventory page
        inventory_page.wait_until_loaded()
        assert inventory_page.is_loaded()

        # Inventory
        inventory = InventoryPage(page)
        inventory.wait_until_loaded()

        #Produkt hinzufügen
        inventory.add_first_item_to_cart()

        #Warenkorb öffnen
        cart = CartPage(page)
        cart.open_cart()
        cart.wait_until_loaded()

        #Validierung
        assert cart.get_cart_count() == 1
        
