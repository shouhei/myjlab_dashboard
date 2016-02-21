import sys
import os
from websocket import create_connection
import json

if __name__ == "__main__":
    sys.path.append(os.getcwd())
    from config import ProductionConfig as Config
    message = "check"
    ws = create_connection(Config.websocket_endpoint()+"/websocket")
    ws.send(json.dumps({"label":"check", "message": message}))
    ws.recv()
    ws.close()
