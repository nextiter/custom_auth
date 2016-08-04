#!/usr/bin/env python
# -*- coding: utf-8 -*-


#
# client_socket.py
#	
# Заготовка клиентской части программы на сокетах
# Отправлят данные на сервер на 9009 порту
# Получает ответ, что данные получены, печатает его и завершает работу.
#
# 04.08.2016
# author S.Ivakhov <nextiter@gmail.com>
#
import socket
import constants



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((constants.SERVER_HOST, constants.PORT))


client_socket.sendall('Hello, world2')
data = client_socket.recv(1024)
print 'Received', data.decode('utf-8')
client_socket.close()