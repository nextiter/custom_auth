#!/usr/bin/env python
# -*- coding: utf-8 -*-


#
# server_socket.py
# Заготовка серверной части программы на сокетах
# Сейчас она ожидает данные на 9009 порту
# разрешает авторизацию, если данные ID карты есть в базе данных и сотрудник с таким ID имеет уровень доступа больше 20
#
# 04.08.2016
# author S.Ivakhov <nextiter@gmail.com>
#

import socket
import constants
import db_worker

db_interface = db_worker.DBWorker()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((constants.SERVER_HOST, constants.PORT))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1)

SKUD_request = {'level': -1}
data = ''
while True:
    conn, addr = server_socket.accept()
    data = conn.recv(1024)
    arm_request = data.decode('utf-8')
    SKUD_request = db_interface.get_emloyee_info(arm_request)
    print SKUD_request
    if not SKUD_request:
        print 'Deny, empty response'
        conn.sendall('DENY')
    elif SKUD_request['level'] > 20:
        conn.sendall('ALLOW')
        print "allow"
        SKUD_request = {'level': -1}
    else:
        conn.sendall('DENY')
        print "deny because ", arm_request
