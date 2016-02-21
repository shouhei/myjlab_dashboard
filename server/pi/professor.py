# coding: utf-8

import serial
import time, sys
from websocket import create_connection

ser = serial.Serial("/dev/cu.usbmodem1411",9600)
host = "ec2-52-193-112-208.ap-northeast-1.compute.amazonaws.com"
def post_professor_status(status):
    ws = create_connection("ws://"+host+"/websocket")
    json_data = {'label':"professor", 'status':status, "time": time.strftime("%m月%M日%H時%M分")}
    print("post websocket")
    print(ws.send(str(json_data)))
    print(ws.recv())
    ws.close()

if __name__ =="__main__":
    print("reading...")
    while True:
        read_ser = ser.readline()
        status = read_ser.decode('utf-8')[:-2]
        post_professor_status(status)
#        time.sleep(10)
