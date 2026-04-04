from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str
    ENV: str = "dev"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
