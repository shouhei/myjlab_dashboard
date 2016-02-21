import sys
import os
import time
import json
from websocket import create_connection
from weather import WeatherAPI

if __name__ == "__main__":
    sys.path.append(os.getcwd())
    from config import ProductionConfig as Config
    weather = WeatherAPI().get_data()
    if weather is not None:
        ws = create_connection(Config.websocket_endpoint()+"/websocket")
        data = weather.to_dict()
        data["time"] = time.strftime("%m月%M日%H時%M分")
        ws.send(json.dumps(data))
        ws.recv()
        ws.close()
