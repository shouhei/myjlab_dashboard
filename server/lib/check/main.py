import sys
import os
from websocket import create_connection

if __name__ == "__main__":
    sys.path.append(os.getcwd())
    from config import VagrantConfig as Config
    message = "check"
    ws = create_connection(Config.websocket_endpoint()+"/websocket")
    ws.send(message)
    ws.recv()
    ws.close()