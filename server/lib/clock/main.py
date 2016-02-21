import sys
import os
import time
from timetable import TimeTable
from websocket import create_connection
import json

if __name__ == "__main__":
    sys.path.append(os.getcwd())
    from config import VagrantConfig as Config
    now = time.localtime()
    message = ""
    for key, row in enumerate(TimeTable.table()):
        if row.is_near_start(now):
            message = str(key + 1) + "限がもうすぐ始まります"
        elif row.is_near_end(now):
            message = str(key + 1) + "限がもうすぐ終わります"
    if message is not "":
        ws = create_connection(Config.websocket_endpoint()+"/websocket")
        ws.send(json.dumps({"label": "time", "message": message, "time": time.strftime("%m月%M日%H時%M分")}))
        ws.recv()
        ws.close()
