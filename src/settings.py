import os
import sys

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    if sys.platform.lower() == "win32" or os.name.lower() in ["nt", "darwin", "posix"]:
        from dotenv import load_dotenv

        load_dotenv()

    bot_token: str = Field(os.environ.get("BOT_TOKEN"))

    db_engine: str = Field(os.environ.get("DB_ENGINE"))
    db_user: str = Field(os.environ.get("DB_USER"))
    db_password: str = Field(os.environ.get("DB_PASSWORD"))
    db_host: str = Field(os.environ.get("DB_HOST"))
    db_port: int = Field(os.environ.get("DB_PORT"))
    db_name: str = Field(os.environ.get("DB_NAME"))

    fatsecret_id: str = Field(os.environ.get("FATSECRET_ID"))
    fatsecret_key: str = Field(os.environ.get("FATSECRET_KEY"))



    @property
    def database_url(self) -> str:
        return f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        


settings: Settings | None = None


def get_settings() -> Settings:
    """
    Возвращает глобальные настройки проекта
    """
    global settings

    if not settings:
        settings = Settings()
    return settings
