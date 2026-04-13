from playwright.sync_api import Page,expect


class CartPage:
    def __init__(self, page: Page):
        
        # =========================================
        # Vorbedingung (Initialisierung)
        # =========================================
        # Übergabe des Playwright Page-Objekts
        # Dieses Objekt steuert die gesamte Browser-Interaktion
        self.page = page
        
        # Locator für den Warenkorb-Button (oben rechts)
        self.cart_link = page.locator(".shopping_cart_link")
        # Locator für alle Produkte im Warenkorb
        self.cart_items = page.locator(".cart_item")

    def open_cart(self):
        
        # =========================================
        # Aktion: Warenkorb öffnen
        # =========================================
        expect(self.cart_link).to_be_visible()
        self.cart_link.click()

    def wait_until_loaded(self):
        
        # Prüfen, ob der Warenkorb-Button sichtbar ist
        expect(self.cart_items.first).to_be_visible()

    def get_cart_count(self):
        # Klick auf den Warenkorb
        return self.cart_items.count()
    
    # =========================================
    # Erwartung: Warenkorb geladen
    # =========================================
    def wait_until_loaded(self):

        # Warten bis mindestens ein Produkt im Warenkorb sichtbar ist
        expect(self.cart_items.first).to_be_visible()

    # =========================================
    # Daten abrufen
    # =========================================
    def get_cart_count(self):

        # Gibt die Anzahl der Produkte im Warenkorb zurück
        return self.cart_items.count()
    
    