import time
from ticklog import *

if __name__ == "__main__":
    start_time = time.time()
    binance = GetData()
    key = binance.get_tick_data("ETHBTC")
    key2 = binance.get_tick_data("BTCUSDT")
    binance.socket.start()
