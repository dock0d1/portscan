#!/usr/bin/env python
import socket 

host = str(input('HOST: '))

ports = [21,22,80,443,3306,110]

for port in ports:
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)
    resp = sk.connect_ex((host,port))
    if resp == 0:
        print('PORT ABERTA {}'.format (port)) 
    else:
        print('PORTA FECHADA {}'.format(port))

sk.close()