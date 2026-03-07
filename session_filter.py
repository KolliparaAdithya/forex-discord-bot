import datetime

def is_trading_session():

    now = datetime.datetime.utcnow()
    hour = now.hour

    if 7 <= hour <= 16:
        return True

    if 13 <= hour <= 22:
        return True

    return False