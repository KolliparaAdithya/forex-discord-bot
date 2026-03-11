import datetime

from discord_bot import send_bot_status, send_daily_report, send_signal
from data_fetcher import get_data
from indicators import add_indicators
from strategy import check_signal
from risk_manager import can_take_trade, record_trade
from session_filter import is_trading_session
from stats import record_signal

pairs = [ "XAU/USD","EUR/USD","GBP/USD","USD/JPY","AUD/USD","USD/CAD","NZD/USD","EUR/JPY","GBP/JPY","AUD/JPY" ]


def scan_market():

    today = datetime.datetime.today().weekday()

    if today >= 5:
        print("Weekend detected - Forex market closed")
        return

    if not is_trading_session():
        print("Outside trading session")
        return

    print("\nScanning market...")

    for pair in pairs:

        print(f"Checking {pair}")

        if not can_take_trade():
            print("Daily trade limit reached")
            return

        h4 = get_data(pair, "4h")
        h1 = get_data(pair, "1h")
        m15 = get_data(pair, "15min")
        m5 = get_data(pair, "5min")

        if h4 is None or h1 is None or m15 is None or m5 is None:
            print("Data fetch failed")
            continue

        h4 = add_indicators(h4)
        h1 = add_indicators(h1)
        m15 = add_indicators(m15)
        m5 = add_indicators(m5)

        signal = check_signal(h4, h1, m15, m5)

        if signal:

            price = m5.iloc[-1].close

            risk = 5
            reward = 15

            if signal == "BUY":
                entry = price
                sl = price - risk
                tp = price + reward
            else:
                entry = price
                sl = price + risk
                tp = price - reward

            print(f"Signal found → {pair} {signal}")

            send_signal(pair, signal, entry, sl, tp)

            record_trade()
            record_signal()


print("===================================")
print(" Forex AI Signal Bot Started 🚀")
print(" GitHub Scheduled Execution")
print("===================================")

now = datetime.datetime.utcnow()

# Send bot active message once per day
if now.hour == 0 and now.minute < 5:
    send_bot_status()

# Send daily report
if now.hour == 23 and now.minute > 55:
    send_daily_report()

scan_market()
