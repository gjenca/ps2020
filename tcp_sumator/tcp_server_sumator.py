#!/usr/bin/env python3
import socket
import os
import sys
import re

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("",9999))
s.listen(5)
while True:
    conn_s,addr=s.accept()
    print("Pripojil sa klient",addr)
    if not os.fork():
        s.close()
        f=conn_s.makefile(mode="rw",encoding="utf-8")
        summa=0
        while True:
            line=f.readline()
            if not line:
                break
            line=line.strip()
            print("Klient poslal",">>>%s<<<" % line)
            if line=="QUIT":
                f.write("101 Bye\n")
                f.flush()
                break
            elif line=="SUM":
                f.write("100 OK\n")
                f.write("%d\n" % summa)
                f.flush()
                continue
            elif line=="ZERO":
                summa=0
                f.write("100 OK\n")
                f.flush()
                continue
            m=re.match(r"NUMBER +(.+)",line)
            if m:
                if not (m.group(1)).isdigit():
                    f.write("200 Not a number\n")
                    f.flush()
                    continue
                num=int(m.group(1))
                summa=summa+num
                f.write("100 OK\n")
                f.flush()
                continue
            f.write("201 Bad request\n")
            f.flush()
        conn_s.close()
        sys.exit(0)
    else:
        conn_s.close()

