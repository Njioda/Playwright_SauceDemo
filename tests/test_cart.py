from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart_and_verify(page):

    # =========================================
    # Vorbedingung: Login
    # =========================================
    
    # LoginPage Objekt erstellen
    login_page = LoginPage(page)
    
    # Login-Seite öffnen
    login_page.navigate()
    
    # Login mit gültigen Daten durchführen
    login_page.login("standard_user", "secret_sauce")

    # =========================================
    # Inventory Seite
    # =========================================
    
    # Warten bis Produkte geladen sind
    inventory = InventoryPage(page)
    
    # Warten bis Produkte geladen sind
    inventory.wait_until_loaded()
    # Prüfen, ob Inventory korrekt geladen wurde
    assert inventory.is_loaded()

    # =========================================
    # Aktion: Produkt hinzufügen
    # =========================================
    inventory.add_first_item_to_cart()

    # =========================================
    #  Warenkorb öffnen
    # =========================================
    cart = CartPage(page)
    
    # Warenkorb öffnen
    cart.open_cart()
    
    # Warten bis Warenkorb geladen ist
    cart.wait_until_loaded()
    
    # =========================================
    # Validierung
    # =========================================
    # Prüfen, ob genau 1 Produkt im Warenkorb ist
    assert cart.get_cart_count() == 1