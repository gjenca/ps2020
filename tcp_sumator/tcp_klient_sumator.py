#!/usr/bin/env python3

import socket
import sys

def check_status_100_or_exit(line):
    
    line_splitted=line.split(maxsplit=1)
    if line_splitted:
        if line_splitted[0]!="100":
            print("Server error:%s" % line.strip(),file=sys.stderr)
            sys.exit(1)


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",9999))
f=s.makefile(encoding="utf-8",mode="rw")
for num in range(1,101):
    f.write("NUMBER %d\n" % num)
    f.flush()
    line=f.readline()
    check_status_100_or_exit(line)
f.write("SUM\n")
f.flush()
line=f.readline()
check_status_100_or_exit(line)
line=f.readline()
print("Sucet cisel je",line.strip())



