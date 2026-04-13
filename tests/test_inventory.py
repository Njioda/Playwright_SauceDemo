from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_loaded(page):  
        """
    Testet den erfolgreichen Login und die vollständige Anzeige
    der Inventory-Seite inklusive Produktvalidierung.
    """
        # Page Objects initialisieren
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        
        # Navigation zur Login-Seite
        login_page.navigate()
        # Login mit gültigen Credentials
        login_page.login("standard_user", "secret_sauce")

        # Warten bis Inventory-Seite geladen ist
        inventory_page.wait_until_loaded()
        # Sicherstellen, dass Produkte geladen wurden
        assert inventory_page.is_loaded()

        # Überprüfen, dass genau 6 Produkte vorhanden sind
        inventory_page.assert_item_count(6)

        # Check product names
        actual_products = inventory_page.get_all_product_names()
        expected_products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]
        
       # Tatsächliche Produktnamen auslesen
        actual_products = inventory_page.get_all_product_names()
        
        # 🔹 Vergleich: Erwartete vs. tatsächliche Produkte
        assert actual_products == expected_products

        # Vollständige UI-Validierung aller Produkte:
        # Name vorhanden
        # Preis korrekt formatiert
        # Add-to-cart Button sichtbar & aktiv
        inventory_page.validate_products_ui()

        


if __name__ == "__main__":
    test_inventory_loaded()