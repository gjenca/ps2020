#!/usr/bin/python3
import socket

IP_ADDR="mpm.svf.stuba.sk"
PORT=9999

string_to_send="1+2+17"

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(string_to_send.encode("utf-8"),(IP_ADDR,PORT))
data,addr=s.recvfrom(1024)
cislo=int(data.decode("utf-8"))
print(cislo)

