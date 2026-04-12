from playwright.sync_api import Page
from playwright.sync_api import expect
import re

class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.items = page.locator('[data-test="inventory-item-name"]')
        self.items = page.locator('[data-test="inventory-item"]')
        self.product_names = page.locator('[data-test="inventory-item-name"]')

    def wait_until_loaded(self):
        expect(self.items.first).to_be_visible()

    def is_loaded(self):
        return self.items.count() > 0
    
    def assert_item_count(self, expected: int):
        expect(self.items).to_have_count(expected)
        
    def get_all_product_names(self):
        return self.product_names.all_text_contents()
    
    def add_first_item_to_cart(self):
        #klick auf erstes "Add to cart"
        self.page.locator('button[data-test^="add-to-cart"]').first.click()
    
    # 🔥 NEU: Vollständige Validierung aller Produkte
    def validate_products_ui(self):
        count = self.items.count()
        assert count > 0, "❌ Keine Produkte gefunden!"

        for i in range(count):
            item = self.items.nth(i)

            # 🔹 Produktname
            name_locator = item.locator('[data-test="inventory-item-name"]')
            expect(name_locator).to_be_visible()
            name = name_locator.inner_text().strip()
            assert name != "", f"❌ Leerer Produktname bei Index {i}"

            # 🔹 Preis
            price_locator = item.locator('.inventory_item_price')
            expect(price_locator).to_be_visible()
            price_text = price_locator.inner_text()

            assert re.match(r"^\$\d+\.\d{2}$", price_text), \
                f"❌ Ungültiger Preis bei {name}: {price_text}"

            # 🔹 Add-to-cart Button
            button = item.locator('button[data-test^="add-to-cart"]')
            expect(button).to_be_visible()
            expect(button).to_be_enabled()
    
    

    #def open_menu(self):
        #self.menu_button.click()
        #self.menu.wait_for()

    #def logout(self):
        #self.logout_link.click()