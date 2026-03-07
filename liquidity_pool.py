def detect_liquidity_pool(df):

    highs = df["high"].tail(10)
    lows = df["low"].tail(10)

    equal_highs = highs.max() - highs.min() < 0.0003
    equal_lows = lows.max() - lows.min() < 0.0003

    if equal_highs:
        return "SELL_LIQUIDITY"

    if equal_lows:
        return "BUY_LIQUIDITY"

    return None