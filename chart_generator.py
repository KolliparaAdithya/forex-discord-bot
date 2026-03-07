import mplfinance as mpf
import pandas as pd

def generate_chart(df, pair):

    df = df.tail(50)

    df.index = pd.to_datetime(df.index)

    filename = f"{pair}_chart.png"

    mpf.plot(
        df,
        type='candle',
        style='charles',
        title=pair,
        volume=False,
        savefig=filename
    )

    return filename