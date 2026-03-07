def detect_trend(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    # bullish trend
    if last.close > prev.close:
        return "BUY"

    # bearish trend
    if last.close < prev.close:
        return "SELL"

    return None