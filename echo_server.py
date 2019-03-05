#!/usr/bin/env python3

import socket

TCP_IP = '172.19.29.141'
TCP_PORT = 30000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

f = open ("DataStream.csv", "w")

conn, addr = s.accept()
print ('Connection address:', addr)
print("Writting in DataStream.csv, Press ctrl + c to stop")
while 1:
    data = conn.recv(BUFFER_SIZE) 
    stringdata = data.decode('utf-8')
    #f.write(data)  # echo
    if not data: break
    print ("received data:", data)
    stringdata = stringdata.replace("(","")
    stringdata = stringdata.replace(")","\n")
    conn.send(data)  # echo
    f.write(stringdata)  # echo
conn.close()
