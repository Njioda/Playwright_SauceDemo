from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        
         # ================================
         #  Vorbedingung 
         # ================================
        
        # Übergabe des Playwright Page-Objekts
        # Dieses Objekt wird für alle Interaktionen mit der Webseite verwendet
        self.page = page
        
        # Lokatoren für die Login-Elemente definieren
        # Eingabefeld für Benutzername 
        self.username_input = page.get_by_placeholder("Username")
        # Eingabefeld für Passwort
        self.password_input = page.get_by_placeholder("Password")
        # Login-Button
        self.login_button = page.get_by_role("button", name="Login")
        

    def navigate(self):
        # Navigation zur Login-Seite von SauceDemo
        self.page.goto("https://www.saucedemo.com/")
    
        # ================================
        #  Aktion
        # ================================
       

    def login(self, username: str, password: str):
       # Aktion: Benutzer meldet sich an
        
       # Benutzername in das Eingabefeld eintragen
        self.username_input.fill(username)
       # Passwort in das Eingabefeld eintragen
        self.password_input.fill(password)
       # Klick auf den Login-Button
        self.login_button.click()
        
        
    def wait_until_loaded(self):
       # Warten bis die Zielseite (Inventory) geladen ist
       # Dies stellt sicher, dass der Login-Prozess abgeschlossen ist
        self.page.wait_for_url("**/inventory.html")
    
       # ================================
       # Verhalten / Erwartung (Expected Behavior)
       # ================================

    def is_loaded(self):
       # Prüft, ob die aktuelle URL auf die Inventory-Seite endet
       # → bedeutet: Login war erfolgreich
        return self.page.url.endswith("inventory.html")
    
    
   