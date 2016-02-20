import sys
import os
import time
from timetable import TimeTable
from websocket import create_connection

if __name__ == "__main__":
    sys.path.append(os.getcwd())
    from config import DevelopConfig
    now = time.localtime()
    message = ""
    for key, row in enumerate(TimeTable.table()):
        if row.is_near_start(now):
            message = str(key + 1) + "限がもうすぐ始まります"
        elif row.is_near_end(now):
            message = str(key + 1) + "限がもうすぐ終わります"
    if message == "":
        message = "nothing"
    if message:
        ws = create_connection("ws://localhost:8888/websocket")
        ws.send(message)
        ws.recv()
        ws.close()
