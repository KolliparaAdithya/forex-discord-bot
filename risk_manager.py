import datetime

trade_count = 0
current_day = datetime.date.today()

def can_take_trade():

    global trade_count, current_day

    today = datetime.date.today()

    if today != current_day:
        trade_count = 0
        current_day = today

    return trade_count < 3


def record_trade():
    global trade_count
    trade_count += 1