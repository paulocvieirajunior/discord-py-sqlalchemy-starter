from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str
    OWNER_ID: int | None = None
    ENV: str = "dev"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
