from storage.user_profile import UserProfile
import sqlite3

def test_user_creation_and_db(monkeypatch):
    """
    Prueba la creación de un usuario y el guardado en base de datos usando un mock de sqlite3.

    Crea una instancia de UserProfile y simula la conexión a la base de datos con monkeypatch.
    Verifica que el método save_to_db() se ejecute correctamente sin errores de conexión real.

    Parámetros
    ----------
    monkeypatch : pytest.MonkeyPatch
        Utilidad de pytest para reemplazar objetos durante la prueba.

    Returns
    -------
    None
    """
    user = UserProfile("TestUser", 25, 170, 65, 14.0, "cardio")

    def mock_connect(*args, **kwargs):
        class Cursor:
            def execute(self, *args): return None
            def close(self): pass
            def fetchone(self): return [user.user_id, user.name]
        class Conn:
            def cursor(self): return Cursor()
            def commit(self): pass
            def close(self): pass
        return Conn()

    monkeypatch.setattr(sqlite3, "connect", mock_connect)
    user.save_to_db()