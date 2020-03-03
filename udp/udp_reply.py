#!/usr/bin/python3
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",9999))
data,addr=s.recvfrom(1024)
string_received=data.decode("utf-8")
print(string_received)
result=eval(string_received)
print(result)
result_bytes=str(result).encode("utf-8")
s.sendto(result_bytes,addr)

