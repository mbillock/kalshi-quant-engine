"""
Market data feed.

Receives market updates from Kalshi and distributes them
to the rest of the application.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class MarketUpdate:
    ticker: str
    yes_bid: float
    yes_ask: float
    no_bid: float
    no_ask: float
    timestamp: datetime


class MarketFeed:
    def __init__(self):
        self.latest = {}

    def update(self, update: MarketUpdate):
        self.latest[update.ticker] = update

    def get(self, ticker: str):
        return self.latest.get(ticker)
