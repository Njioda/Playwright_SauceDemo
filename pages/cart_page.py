from playwright.sync_api import Page,expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_items = page.locator(".cart_item")

    def open_cart(self):
        expect(self.cart_link).to_be_visible()
        self.cart_link.click()

    def wait_until_loaded(self):
        expect(self.cart_items.first).to_be_visible()

    def get_cart_count(self):
        return self.cart_items.count()
    
    