#!/usr/bin/env python
# -*- coding: utf-8 -*-


#
# server_socket.py
# Заготовка серверной части программы на сокетах
# Сейчас она ожидает данные на 9009 порту
# разрешает авторизацию, если данные равны ID моей карты и запрещает во всех остальных случаях
#
# 04.08.2016
# author S.Ivakhov <nextiter@gmail.com>
#

import socket
import constants

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((constants.SERVER_HOST, constants.PORT))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1)


data = ''
while True:
    conn, addr = server_socket.accept()
    data = conn.recv(1024)
    arm_request = data.decode('utf-8')
    if arm_request == '8204887':
        conn.sendall('ALLOW')
        print "allow"
    else:
        conn.sendall('DENY')
        print "deny because ", arm_request
