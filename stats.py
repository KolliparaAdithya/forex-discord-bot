signals_today = 0
wins_today = 0
losses_today = 0


def record_signal():
    global signals_today
    signals_today += 1


def record_win():
    global wins_today
    wins_today += 1


def record_loss():
    global losses_today
    losses_today += 1


def get_daily_stats():
    return signals_today, wins_today, losses_today
