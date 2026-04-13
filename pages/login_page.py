from playwright.sync_api import Page


class LoginPage:
    # ==========================================
    # Initialisierung der LoginPage
    # ==========================================
    def __init__(self, page: Page):
        # Playwright Page-Objekt wird übergeben
        # Damit werden alle Interaktionen mit der Webseite gesteuert
        self.page = page

        # =========================
        # Locator (UI-Elemente)
        # =========================

        # Eingabefeld für Benutzername
        self.username_input = page.get_by_placeholder("Username")

        # Eingabefeld für Passwort
        self.password_input = page.get_by_placeholder("Password")

        # Login-Button
        self.login_button = page.get_by_role("button", name="Login")

        # Fehlernachricht (wird bei Login-Fehlern angezeigt)
        self.error_message = page.locator('[data-test="error"]')

    # ==========================================
    # Navigation
    # ==========================================
    def navigate(self):
        # Öffnet die Login-Seite der Anwendung
        self.page.goto("https://www.saucedemo.com/")

    # ==========================================
    # Aktionen (User Interactions)
    # ==========================================
    def login(self, username: str, password: str):
        # Benutzername eingeben
        self.username_input.fill(username)

        # Passwort eingeben
        self.password_input.fill(password)

        # Login-Button klicken
        self.login_button.click()

    # ==========================================
    # Positive Validierung
    # ==========================================
    def is_logged_in(self):
        # Prüft, ob der Login erfolgreich war
        # Erfolg = Weiterleitung auf Inventory-Seite
        return self.page.url.endswith("inventory.html")

    def wait_until_loaded(self):
        # Wartet bis die Inventory-Seite geladen ist
        self.page.wait_for_url("**/inventory.html")

    # ==========================================
    # Negative Validierung (Fehlerfälle)
    # ==========================================
    def is_error_visible(self):
        # Prüft, ob eine Fehlermeldung sichtbar ist
        return self.error_message.is_visible()

    def get_error_message(self):
        # Gibt den Text der Fehlermeldung zurück
        return self.error_message.text_content()

    def wait_for_error(self):
        # Wartet, bis die Fehlermeldung erscheint
        self.error_message.wait_for(state="visible")