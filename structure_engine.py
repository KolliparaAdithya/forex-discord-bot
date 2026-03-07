def detect_market_structure(df):

    highs = df["high"].tail(5).values
    lows = df["low"].tail(5).values

    # Higher High + Higher Low → bullish structure
    if highs[-1] > highs[-2] and lows[-1] > lows[-2]:
        return "HH_HL"

    # Lower Low + Lower High → bearish structure
    if highs[-1] < highs[-2] and lows[-1] < lows[-2]:
        return "LL_LH"

    return None