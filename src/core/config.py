import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


# Загружаем основной файл окружения
dotenv.load_dotenv()


class Settings(BaseSettings):

    DB_URL: str

    TOKEN: str

    model_config = SettingsConfigDict(env_file="/.env")


settings = Settings()
