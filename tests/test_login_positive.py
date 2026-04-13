from pages.login_page import LoginPage


# =========================================
# POSITIVER LOGIN TEST
# =========================================
# Ziel:
# Prüfen, ob ein gültiger Benutzer sich erfolgreich einloggen kann
# und auf die Inventory-Seite weitergeleitet wird
# =========================================
def test_login_and_inventory_validation(page):

    # =========================
    # Arrange (Vorbereitung)
    # =========================

    # LoginPage Objekt erstellen (Page Object Model)
    login_page = LoginPage(page)

    # Öffnen der Login-Seite
    login_page.navigate()

    # =========================
    # Act (Aktion)
    # =========================

    # Eingabe gültiger Login-Daten
    login_page.login("standard_user", "secret_sauce")

    # =========================
    # Assert (Überprüfung)
    # =========================

    # Warten bis die Inventory-Seite geladen ist
    login_page.wait_until_loaded()

    # Prüfen, ob der Login erfolgreich war
    assert login_page.is_logged_in()