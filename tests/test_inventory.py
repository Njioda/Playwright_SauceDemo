from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
from page.inventory_page import InventoryPage


def test_inventory_loaded(page):
    
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        # Wait for inventory page
        inventory_page.wait_until_loaded()
        assert inventory_page.is_loaded()

        # Check item count
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

        assert actual_products == expected_products

        # Validate UI
        inventory_page.validate_products_ui()

        


if __name__ == "__main__":
    test_inventory_loaded()