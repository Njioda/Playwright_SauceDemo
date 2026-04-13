from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_and_inventory_validation(page):
    
        # =========================================
        # Vorbedingung
        # =========================================
        
        # LoginPage Objekt erstellen (Page Object Model)
        login_page = LoginPage(page)
        
        # =========================================
        #  Aktion
        # =========================================
        
        # Öffnen der Login-Seite
        login_page.navigate()

        # Eingabe gültiger Login-Daten
        login_page.login("standard_user", "secret_sauce")
        
        # Warten bis die Inventory-Seite vollständig geladen ist
        page.wait_for_url("**/inventory.html")
        
        # =========================================
        # Erwartung / Validierung
        # =========================================

        # Prüfen, ob Inventory-Seite korrekt geladen wurde
        login_page.wait_until_loaded()
        
        # Validierung: Login war erfolgreich
        assert login_page.is_loaded()
        
        
        