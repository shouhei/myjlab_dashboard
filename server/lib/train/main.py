import sys
import os
import time
import json
from websocket import create_connection
from train import TragetTrain

if __name__ == "__main__":
    sys.path.append(os.getcwd())
    from config import VagrantConfig as Config
    target_train = TragetTrain.get()
    ws = create_connection(Config.websocket_endpoint()+"/websocket")
    data = {"label": "train", "trains": target_train, "time": time.strftime("%m月%M日%H時%M分")}
    ws.send(json.dumps(data))
    ws.recv()
    ws.close()
