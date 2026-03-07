def detect_entry(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    # Liquidity sweep below previous low → BUY
    if last["low"] < prev["low"] and last["close"] > prev["low"]:
        return "BUY"

    # Liquidity sweep above previous high → SELL
    if last["high"] > prev["high"] and last["close"] < prev["high"]:
        return "SELL"

    return None