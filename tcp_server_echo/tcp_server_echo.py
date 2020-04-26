#!/usr/bin/env python3
import socket
import os
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("",9999))
s.listen(5)
while True:
    conn_s,addr=s.accept()
    if not os.fork():
        s.close()
        f=conn_s.makefile(mode="rw",encoding="utf-8")
        while True:
            line=f.readline()
            if not line:
                break
            f.write("ECHO:"+line)
            f.flush()
        conn_s.close()
        sys.exit(0)
    else:
        conn_s.close()

