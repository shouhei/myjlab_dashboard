# coding: utf-8

import serial
import time, sys
from websocket import create_connection
import json

ser = serial.Serial("/dev/ttyACM0",9600)
#my_host = "192.168.1.60:8888"
my_host = "ec2-52-193-112-208.ap-northeast-1.compute.amazonaws.com"
def post_professor_status(status):
    ws = create_connection("ws://"+my_host+"/websocket")
    json_data = {"label":"professor", "status":status, "time": time.strftime("%m月%M日%H時%M分")}
    print("post websocket")
    print(ws.send(json.dumps(json_data)))
    print(ws.recv())
    ws.close()

if __name__ =="__main__":
    print("reading...")
    while True:
        read_ser = ser.readline()
        status = read_ser.decode('utf-8')[:-2]
        post_professor_status(status)
#        time.sleep(1)
