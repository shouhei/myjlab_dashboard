import sys
from websocket import create_connection
ws = create_connection("ws://localhost:8888/other_websocket")

if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    message = 'hello world!'

print(ws.send(message))
print(ws.recv())

ws.close()
