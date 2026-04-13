from playwright.sync_api import Page
from playwright.sync_api import expect
import re

class InventoryPage:
    def __init__(self, page):
        self.page = page
        
        # Locator für alle Produkt-Container (jedes Produkt)
        self.items = page.locator('[data-test="inventory-item"]')
        # Locator für alle Produktnamen
        self.product_names = page.locator('[data-test="inventory-item-name"]')
        

    def wait_until_loaded(self):
        """
        Wartet, bis die Inventory-Seite geladen ist,
        indem geprüft wird, ob das erste Produkt sichtbar ist.
        """
        expect(self.items.first).to_be_visible()

    def is_loaded(self):
        """
        Prüft, ob Produkte vorhanden sind.
        Rückgabe: True, wenn mindestens ein Produkt existiert.
        """
        return self.items.count() > 0
    
    def assert_item_count(self, expected: int):
        """
        Verifiziert die Anzahl der angezeigten Produkte.

        :param expected: Erwartete Anzahl von Produkten
        """
        expect(self.items).to_have_count(expected)
        
    def get_all_product_names(self):
        """
        Gibt eine Liste aller Produktnamen zurück.
        """
        return self.product_names.all_text_contents()
    
    def add_first_item_to_cart(self):
        """
        Fügt das erste Produkt der Liste zum Warenkorb hinzu.
        Klickt auf den ersten "Add to cart"-Button.
        """
        self.page.locator('button[data-test^="add-to-cart"]').first.click()
    
    
    def validate_products_ui(self):
        """
        Validiert alle Produkte auf der Inventory-Seite.

        Für jedes Produkt wird geprüft:
        - Produktname ist sichtbar und nicht leer
        - Preis ist sichtbar und im korrekten Format ($xx.xx)
        - "Add to cart" Button ist sichtbar und aktiv
        """
        count = self.items.count()

        # Sicherstellen, dass überhaupt Produkte vorhanden sind
        assert count > 0, " Keine Produkte gefunden!"

        for i in range(count):
            item = self.items.nth(i)

            # 🔹 Produktname prüfen
            name_locator = item.locator('[data-test="inventory-item-name"]')
            expect(name_locator).to_be_visible()

            name = name_locator.inner_text().strip()
            assert name != "", f" Leerer Produktname bei Index {i}"

            # Preis prüfen
            price_locator = item.locator('.inventory_item_price')
            expect(price_locator).to_be_visible()

            price_text = price_locator.inner_text()

            # Validierung des Preisformats (z. B. $29.99)
            assert re.match(r"^\$\d+\.\d{2}$", price_text), \
                f" Ungültiger Preis bei {name}: {price_text}"

            # Add-to-cart Button prüfen
            button = item.locator('button[data-test^="add-to-cart"]')
            expect(button).to_be_visible()
            expect(button).to_be_enabled()
    
    

   