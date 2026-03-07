def detect_liquidity_sweep(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    if last["high"] > prev["high"] and last["close"] < prev["high"]:
        return "SELL"

    if last["low"] < prev["low"] and last["close"] > prev["low"]:
        return "BUY"

    return None