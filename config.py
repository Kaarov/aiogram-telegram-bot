import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

settings = Settings(bot_token=BOT_TOKEN)
