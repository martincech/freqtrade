from typing import List, Tuple, Dict

from freqtrade.enums import MarginMode, TradingMode
from freqtrade.exchange import Exchange


class Xtb(Exchange):
    _supported_trading_mode_margin_pairs: List[Tuple[TradingMode, MarginMode]] = [
        (TradingMode.FUTURES, MarginMode.ISOLATED),
        (TradingMode.MARGIN, MarginMode.ISOLATED)
    ]

    _ft_has: Dict = {
        "ohlcv_candle_limit": 100,
        "ohlcv_partial_candle": False,
        "ohlcv_require_since": True,
    }
