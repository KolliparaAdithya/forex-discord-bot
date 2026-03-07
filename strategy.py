from trend import detect_trend
from structure_engine import detect_market_structure
from liquidity_pool import detect_liquidity_pool
from structure import detect_bos
from entry import detect_entry


def check_signal(h4, h1, m15, m5):

    trend_h4 = detect_trend(h4)
    trend_h1 = detect_trend(h1)

    structure = detect_market_structure(h1)

    liquidity = detect_liquidity_pool(m15)

    bos = detect_bos(m15)

    entry = detect_entry(m5)

    if (
        trend_h4 == "BUY"
        and trend_h1 == "BUY"
        and structure == "HH_HL"
        and liquidity == "BUY_LIQUIDITY"
        and bos == "BUY"
        and entry == "BUY"
    ):
        return "BUY"

    if (
        trend_h4 == "SELL"
        and trend_h1 == "SELL"
        and structure == "LL_LH"
        and liquidity == "SELL_LIQUIDITY"
        and bos == "SELL"
        and entry == "SELL"
    ):
        return "SELL"

    return None