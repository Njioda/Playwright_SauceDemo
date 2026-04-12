from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart_and_verify(page):

    # 🔐 Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 📦 Inventory
    inventory = InventoryPage(page)
    inventory.wait_until_loaded()
    assert inventory.is_loaded()

    # 🛒 Produkt hinzufügen
    inventory.add_first_item_to_cart()

    # 🧺 Cart
    cart = CartPage(page)
    cart.open_cart()
    cart.wait_until_loaded()

    # ✅ Validierung
    assert cart.get_cart_count() == 1