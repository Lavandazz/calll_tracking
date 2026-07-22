from pydantic_settings import BaseSettings, SettingsConfigDict
from config.settings_folder import PathFolder


class Settings(BaseSettings):
    """
    Класс для хранения настроек приложения.
    Содержит настройки для подключения к базе данных и другие общие настройки.
    """
    model_config = SettingsConfigDict(env_file=PathFolder.env, env_file_encoding="utf-8")

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int


    def get_sync_db_url(self):
        return (f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
                f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}")


settings = Settings() # type: ignore

print("Settings loaded successfully", settings.POSTGRES_HOST)