# coding: utf-8

###########################

# 201用輝度センサで取得しデータをソケット

##########################
import serial
import time, sys
from websocket import create_connection

ser = serial.Serial("/dev/tty.usbmodem1421",9600)

def post_professor_status(status):
    ws = create_connection("ws://localhost:8888/websocket")
    json_data = {'status':status}
    print("post wensocket")
    print(ws.send(str(json_data)))
    print(ws.recv())
    ws.close()

if __name__ =="__main__":
    print("reading...")
    while True:
        read_ser = int(ser.readline())
        print(read_ser)
        if read_ser > 600: #しきい値の調整
            status = "out"
        else:
            status = "in"
        print(status)
        post_professor_status(status)
        time.sleep(10) #実際は60でやる
