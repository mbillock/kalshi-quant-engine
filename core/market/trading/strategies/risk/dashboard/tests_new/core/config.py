"""
Application configuration management.
Loads settings from environment variables.
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_name: str = "Kalshi Quant Engine"

    kalshi_api_key: str | None = os.getenv(
        "KALSHI_API_KEY"
    )

    kalshi_api_secret: str | None = os.getenv(
        "KALSHI_API_SECRET"
    )

    mode: str = os.getenv(
        "TRADING_MODE",
        "paper"
    )


settings = Settings()
