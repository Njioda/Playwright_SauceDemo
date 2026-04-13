from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_flow(page):

    # =========================================
    # LOGIN
    # =========================================
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    login_page.wait_until_loaded()
    assert login_page.is_logged_in(), "Login fehlgeschlagen"

    # =========================================
    # INVENTORY
    # =========================================
    inventory = InventoryPage(page)
    inventory.wait_until_loaded()

    assert inventory.is_loaded(), "Inventory wurde nicht geladen"

    inventory.add_first_item_to_cart()

    # =========================================
    # CART
    # =========================================
    cart = CartPage(page)
    cart.open_cart()
    cart.wait_until_loaded()

    assert cart.get_cart_count() == 1, "Warenkorb ist leer oder falsch"

    # =========================================
    # CHECKOUT
    # =========================================
    checkout = CheckoutPage(page)
    checkout.click_checkout()

    checkout.wait_for_checkout_info()
    checkout.fill_checkout_info("John", "Doe", "12345")

    checkout.wait_for_overview()
    checkout.finish_checkout()

    # =========================================
    # ASSERTION
    # =========================================
    assert checkout.is_order_complete(), "Bestellung wurde nicht abgeschlossen"