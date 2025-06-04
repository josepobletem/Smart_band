from storage.user_profile import UserProfile
import sqlite3

def test_user_creation_and_db(monkeypatch):
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