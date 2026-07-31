from .base import Strategy


class CryptoStrategy(Strategy):

    def on_market_update(self, market_update):

        print(
            f"{market_update.ticker} "
            f"YES {market_update.yes_bid:.2f}/"
            f"{market_update.yes_ask:.2f}"
        )
