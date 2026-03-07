def detect_bos(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]
    prev2 = df.iloc[-3]

    if last.high > prev.high and prev.high > prev2.high:
        return "BUY"

    if last.low < prev.low and prev.low < prev2.low:
        return "SELL"

    return None