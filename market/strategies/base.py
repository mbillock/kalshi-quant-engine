"""
Base class for trading strategies.
"""

from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def on_market_update(self, market_update):
        """Called whenever new market data arrives."""
        pass
