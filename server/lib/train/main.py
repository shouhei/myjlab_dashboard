import sys
import os
import time
import json
from websocket import create_connection
from train import TragetTrain

if __name__ == "__main__":
    target_train = TragetTrain.get()
    if len(target_train) > 0:
        ws = create_connection("ws://localhost:8888/websocket")
        ws.send(json.dumps(target_train))
        ws.recv()
        ws.close()
