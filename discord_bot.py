import requests
import datetime

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1480125624495505510/lA396_vobirPR2OsdeRSQHUfnGgIOFQvczLj2MxI5GfYCyx7w9hzh80n1etTDgL6mCjv"

daily_signals = 0
daily_wins = 0
daily_losses = 0


def get_session():
    hour = datetime.datetime.utcnow().hour

    if 7 <= hour < 12:
        return "London"

    elif 13 <= hour < 17:
        return "New York"

    return "Off Session"


def send_signal(pair, direction, entry, sl, tp):

    global daily_signals
    daily_signals += 1

    pair_symbol = pair.replace("/", "")
    chart_url = f"https://www.tradingview.com/chart/?symbol=OANDA:{pair_symbol}"

    session = get_session()

    rr = round(abs(tp - entry) / abs(entry - sl), 2)

    data = {
        "embeds": [
            {
                "title": f"GOLDEN ZONE ALERT - {pair_symbol}",
                "description": f"[View Chart]({chart_url})",
                "color": 16753920,
                "fields": [

                    {
                        "name": "Direction",
                        "value": direction,
                        "inline": True
                    },

                    {
                        "name": "Timeframe",
                        "value": "M5",
                        "inline": True
                    },

                    {
                        "name": "Entry",
                        "value": str(entry),
                        "inline": False
                    },

                    {
                        "name": "Stop Loss",
                        "value": str(sl),
                        "inline": True
                    },

                    {
                        "name": "Take Profit",
                        "value": str(tp),
                        "inline": True
                    },

                    {
                        "name": "RR",
                        "value": f"1:{rr}",
                        "inline": True
                    },

                    {
                        "name": "Session",
                        "value": session,
                        "inline": True
                    },

                    {
                        "name": "Setup",
                        "value": "BOS + Liquidity Sweep + FVG",
                        "inline": False
                    }

                ],
                "footer": {
                    "text": "Forex AI Signal Bot"
                }
            }
        ]
    }

    requests.post(WEBHOOK_URL, json=data)


def send_bot_status():

    now = datetime.datetime.utcnow()

    data = {
        "content": f"🟢 **Forex Bot Active**\nDate: {now.date()} UTC\nBot is running and scanning the market."
    }

    requests.post(WEBHOOK_URL, json=data)


def send_daily_report():

    global daily_signals, daily_wins, daily_losses

    if daily_signals == 0:
        winrate = 0
    else:
        winrate = round((daily_wins / daily_signals) * 100, 2)

    data = {
        "content": f"""📊 **Daily Forex Bot Report**

Signals Sent: {daily_signals}
Wins: {daily_wins}
Losses: {daily_losses}
Win Rate: {winrate}%"""
    }

    requests.post(WEBHOOK_URL, json=data)

    daily_signals = 0
    daily_wins = 0
    daily_losses = 0
