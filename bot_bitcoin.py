import websocket
import bitstamp.client
import json
import credentials

def client():
    trading_client = bitstamp.client.Trading(username=credentials.USERNAME, key=credentials.KEY, secret=credentials.SECRET)
    return trading_client


def buy(quantidade):
    trading_client = client()
    trading_client.buy_market_order(amount=quantidade)


def sell(quantidade):
    trading_client = client()
    trading_client.sell_market_order(amount=quantidade)


def on_message(ws, message):

    message = json.loads(message)
    print(message["data"]["price"])


def on_open(ws):
    print("conexão aberta\n")

    request = """{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
    }"""

    ws.send(request)


def on_error(ws, error):
    print(error, "\n")


def on_close(ws, close_status_code, close_msg):
    print("conexão fechada\n")


def on_data(ws):
    print("informaçoes recebidas\n")


def on_ping(ws):
    print("Pingando servidor\n")


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net", on_open=on_open, on_error=on_error,
                                on_close=on_close, on_message=on_message)
    ws.run_forever()
    ws.close()