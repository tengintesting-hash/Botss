import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    bot_token: str
    admin_token: str
    web_app_url: str | None


    @staticmethod
    def from_env() -> "Settings":
        return Settings(
            bot_token=os.getenv("BOT_TOKEN", ""),
            admin_token=os.getenv("ADMIN_TOKEN", ""),
            web_app_url=os.getenv("WEB_APP_URL"),
        )


settings = Settings.from_env()
