from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def capture_chart(pair):

    pair_symbol = pair.replace("/", "")

    url = f"https://www.tradingview.com/chart/?symbol=OANDA:{pair_symbol}"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.set_window_size(1280, 900)

    driver.get(url)

    # wait for chart to load
    time.sleep(8)

    filename = f"{pair_symbol}_chart.png"

    driver.save_screenshot(filename)

    driver.quit()

    return filename