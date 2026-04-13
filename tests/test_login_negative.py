import pytest
from pages.login_page import LoginPage


# ==========================================
# Negative Login Tests (parametrisiert)
# ==========================================
# Ziel:
# Verschiedene ungültige Login-Szenarien prüfen
# (falsches Passwort, leerer Username, gesperrter User usw.)
# ==========================================
@pytest.mark.parametrize("username,password,expected_error", [
    # Falsche Login-Daten (User + Passwort existieren nicht)
    ("invalid_user", "wrong_password", "do not match"),

    # Username fehlt
    ("", "secret_sauce", "Username is required"),

    # Passwort fehlt
    ("standard_user", "", "Password is required"),

    # Gesperrter Benutzer
    ("locked_out_user", "secret_sauce", "locked out"),
])
def test_login_invalid(page, username, password, expected_error):

    # =========================
    # Arrange (Vorbereitung)
    # =========================
    login_page = LoginPage(page)
    login_page.navigate()

    # =========================
    # Act (Aktion)
    # =========================
    login_page.login(username, password)

    # Warten auf Fehlermeldung (Synchronisation)
    login_page.wait_for_error()

    # =========================
    # Assert (Überprüfung)
    # =========================
    assert expected_error in login_page.get_error_message()