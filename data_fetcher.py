import requests
import pandas as pd

API_KEY = "a13905f3cf6e4c79943cc26779a36aa1"

def get_data(pair, timeframe):

    url = f"https://api.twelvedata.com/time_series?symbol={pair}&interval={timeframe}&outputsize=100&apikey={API_KEY}"

    response = requests.get(url).json()

    if "values" not in response:
        return None

    df = pd.DataFrame(response["values"])
    df = df.iloc[::-1]

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)

    return df