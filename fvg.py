def detect_fvg(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]
    prev2 = df.iloc[-3]

    # Bullish FVG
    if prev2.high < last.low:
        return "BUY"

    # Bearish FVG
    if prev2.low > last.high:
        return "SELL"

    return None