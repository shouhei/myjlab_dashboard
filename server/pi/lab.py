# coding: utf-8

import serial
import time, sys
from websocket import create_connection
from ast import literal_eval

#ser = serial.Serial("/dev/tty.usbmodem1421",9600)
ser = serial.Serial("/dev/ttyACM0",9600)

def post_humi_temp(humi,temp):
    ws = create_connection("ws://localhost:8888/websocket")
    json_data = {'label':"lab", 'humid':humi, 'temprature':temp, 'time': time.strftime("%m月%M日%H時%M分") }
    print(ws.send(str(json_data)))
    print(ws.recv())
    ws.close()

def check_alert(alert_status):
    if alert_status == true:
        print("called alert")

if __name__ =="__main__":
    print("reading...")
    while True:
        read_ser = ser.readline()
        read_ser =  literal_eval(read_ser[:11].decode('utf-8'))
        humi = read_ser[1]
        temp = read_ser[2]
        print("Humi:",humi,"Temp:",temp)
        post_humi_temp(humi,temp)
        time.sleep(10)
