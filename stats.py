signals_sent = 0

def record_signal():

    global signals_sent

    signals_sent += 1

    print(f"Total signals today: {signals_sent}")