from config.settings_env import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_sessionmaker_from_settings(settings_obj):
    """Создаёт sessionmaker на основе переданного объекта настроек."""
    engine = create_engine(settings_obj.get_sync_db_url(), pool_pre_ping=True)
    print("engine:", engine)
    print("Sessionmaker created successfully with URL:", settings_obj.get_sync_db_url())
    return sessionmaker(bind=engine)

def build_settings_from_dict(data: dict) -> Settings:
    """
    Создаёт экземпляр Settings из словаря с параметрами.
    Используется для динамической загрузки из QSettings.
    """
    # Используем метод construct() для быстрого создания без валидации (или можно через __init__)
    # Но проще создать новый экземпляр, подставив значения через __init__
    # Однако Pydantic v2 требует все поля, поэтому передаём их в конструктор.
    return Settings(
        POSTGRES_DB=data['POSTGRES_DB'],
        POSTGRES_USER=data['POSTGRES_USER'],
        POSTGRES_PASSWORD=data['POSTGRES_PASSWORD'],
        POSTGRES_HOST=data['POSTGRES_HOST'],
        POSTGRES_PORT=data['POSTGRES_PORT'],
    )