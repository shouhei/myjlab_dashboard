import sys
import os
from websocket import create_connection

if __name__ == "__main__":
    sys.path.append(os.getcwd())
    from config import DevelopConfig
    print(DevelopConfig.websocket_endpoint())
    ws = create_connection(DevelopConfig.websocket_endpoint() + "/websocket")

    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = 'hello world!'

    print(ws.send(message))
    print(ws.recv())

    ws.close()
