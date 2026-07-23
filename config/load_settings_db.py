from PySide6.QtCore import QSettings
from config.settings import build_settings_from_dict

# Ключи для QSettings
COMPANY = "YourCompany"
APP_NAME = "YourApp"

def load_settings_from_qsettings():
    """Читает настройки из QSettings и возвращает объект Settings или None."""
    settings = QSettings(COMPANY, APP_NAME)
    host = settings.value("db/host", "")
    port = settings.value("db/port", 5433, type=int)
    dbname = settings.value("db/dbname", "")
    user = settings.value("db/user", "")
    password = settings.value("db/password", "")
    # Если пароль зашифрован, расшифровать (здесь простой base64)
    if password:
        import base64
        password = base64.b64decode(password.encode()).decode()
        print(f"Загружено: host={host}, port={port}, dbname={dbname}, user={user}, password={password}")
    if all([host, dbname, user, password]):
        return build_settings_from_dict({
            'POSTGRES_HOST': host,
            'POSTGRES_PORT': port,
            'POSTGRES_DB': dbname,
            'POSTGRES_USER': user,
            'POSTGRES_PASSWORD': password,
        })
    return None
