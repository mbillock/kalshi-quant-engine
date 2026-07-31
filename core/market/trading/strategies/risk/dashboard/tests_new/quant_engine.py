"""
Kalshi Quant Engine
"""

from core.logger import logger
from core.config import settings


def main():

    logger.info(
        "Starting %s",
        settings.app_name
    )

    logger.info(
        "Trading mode: %s",
        settings.mode
    )

    logger.info(
        "System initialized"
    )


if __name__ == "__main__":
    main()
