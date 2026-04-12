from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        # Checkout Button (aus deinem HTML)
        self.checkout_button = page.locator('[data-test="checkout"]')

        # 🔹 Checkout Step One Felder
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')

        # 🔹 Overview / Finish
        self.finish_button = page.locator('[data-test="finish"]')
        self.success_message = page.locator('[data-test="complete-header"]')

    # 🛒 Klick auf Checkout
    def click_checkout(self):
        expect(self.checkout_button).to_be_visible()
        self.checkout_button.click()

    # Warten bis Checkout Step One geladen ist
    def wait_for_checkout_info(self):
        expect(self.first_name).to_be_visible()

    # 🧾 Formular ausfüllen
    def fill_checkout_info(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()

    # ⏳ Overview laden
    def wait_for_overview(self):
        expect(self.finish_button).to_be_visible()

    # ✅ Bestellung abschließen
    def finish_checkout(self):
        self.finish_button.click()

    # 🎉 Erfolg prüfen
    def is_order_complete(self):
        expect(self.success_message).to_be_visible()
        return "Thank you" in self.success_message.inner_text()