from discord_bot import send_signal

send_signal(
    pair="EUR/USD",
    direction="SELL",
    entry=1.2546,
    sl=1.2570,
    tp=1.2480
)