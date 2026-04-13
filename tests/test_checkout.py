from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_flow(page):

    # =========================================
    # Login (Vorbedingung)
    # =========================================
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Warten bis Inventory geladen ist
    login_page.wait_until_loaded()
    assert login_page.is_loaded(), "Login fehlgeschlagen"

    # =========================================
    # Inventory Seite
    # =========================================
    inventory = InventoryPage(page)
    inventory.wait_until_loaded()

    assert inventory.is_loaded(), "Inventory wurde nicht geladen"

    # Produkt hinzufügen
    inventory.add_first_item_to_cart()

    # =========================================
    # Warenkorb
    # =========================================
    cart = CartPage(page)
    cart.open_cart()
    cart.wait_until_loaded()

    assert cart.get_cart_count() == 1, "Warenkorb ist leer oder falsch"

    # =========================================
    # Checkout starten
    # =========================================
    checkout = CheckoutPage(page)
    checkout.click_checkout()

    checkout.wait_for_checkout_info()

    # =========================================
    # Checkout Daten eingeben
    # =========================================
    checkout.fill_checkout_info("John", "Doe", "12345")

    # =========================================
    # Overview & Abschluss
    # =========================================
    checkout.wait_for_overview()
    checkout.finish_checkout()

    # =========================================
    # Validierung
    # =========================================
    assert checkout.is_order_complete(), "Bestellung wurde nicht abgeschlossen"