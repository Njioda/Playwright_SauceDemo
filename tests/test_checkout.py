from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage


def test_checkout_flow(page):

    # 🔐 Login
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 📦 Inventory
    inventory_page.wait_until_loaded()
    assert inventory_page.is_loaded()

    inventory_page.add_first_item_to_cart()

    # 🧺 Cart
    cart = CartPage(page)
    cart.open_cart()
    cart.wait_until_loaded()

    assert cart.get_cart_count() == 1

    # 💳 Checkout  (✔️ jetzt korrekt IN der Funktion)
    checkout = CheckoutPage(page)
    checkout.click_checkout()
    checkout.wait_for_checkout_info()

    # 🧾 Daten eingeben
    checkout.fill_checkout_info("John", "Doe", "12345")

    # 🔎 Overview
    checkout.wait_for_overview()

    # ✅ Finish
    checkout.finish_checkout()

    # 🎉 Validierung
    assert checkout.is_order_complete()