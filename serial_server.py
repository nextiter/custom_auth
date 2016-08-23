#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#
# serial_server.py
# Локальный сервер АРМ. Ждет команды на управление ламппой и замком и передает их ардуине
# Загружается вместе с ОС и ожидает команды типа start_green, и транслирует их в команду
# для последовательного порта
# 23.08.2016
# author S.Ivakhov <nextiter@gmail.com>
#

import socket
import serial
import time

SERVER_HOST = "127.0.0.1"
CLIENT_HOST = "127.0.0.1"
PORT = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, PORT))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1)

my_serial = serial.Serial("/dev/ttyUSB0", baudrate=9600)
data = ''
while True:
    conn, addr = server_socket.accept()
    data = conn.recv(1024)
    write_request = data.decode('utf-8')
    if write_request == 'start_green':
        my_serial.write('3')
    elif write_request == 'stop_green':
        my_serial.write('7')
    elif write_request == 'start_red':
        my_serial.write('2')
    elif write_request == 'stop_red':
        my_serial.write('6')
    elif write_request == 'open':
        my_serial.write('1')
