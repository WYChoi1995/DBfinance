from binance.client import Client
from binance.websockets import BinanceSocketManager
from apikey import *
import json


def process_message(msg):
    msg_ = [x for x in msg.values()]
    msg_ = json.dumps(msg_)
    filename = msg["s"] + ".json"

    with open(filename, "a") as data:
        data.write(msg_ + "\n")
        data.close()


class GetData:
    def __init__(self):
        self.client = Client(api_key, api_secret)
        self.socket = BinanceSocketManager(self.client)

    def get_tick_data(self, issuecode):
        return self.socket.start_trade_socket(issuecode, process_message)
