from typing import List, Tuple, Dict

from freqtrade.enums import MarginMode, TradingMode, PriceType
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
        "ohlcv_has_history": False,
        "ccxt_futures_name": "future",
    }

    _ft_has_futures: Dict = {
        "mark_ohlcv_timeframe": "4h",
        "funding_fee_timeframe": "8h",
        "stoploss_on_exchange": True,
        "stoploss_order_types": {
            "limit": "limit",
            "market": "market"
        },
        "stop_price_type_field": "triggerBy",
        "stop_price_type_value_mapping": {
            PriceType.LAST: "LastPrice",
            PriceType.MARK: "MarkPrice",
            PriceType.INDEX: "IndexPrice",
        },
    }
