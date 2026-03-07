def detect_golden_zone(df):

    last = df.iloc[-1]

    high = df["high"].tail(20).max()
    low = df["low"].tail(20).min()

    diff = high - low

    fib50 = high - diff * 0.5
    fib618 = high - diff * 0.618

    if fib618 <= last.close <= fib50:
        return True

    return None