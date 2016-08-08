#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Заготовка для программы
# Все блоки комментариев начианющихся с TODO - необходимо заменить на работающие части программы

import serial
import socket
import constants
# from __future__ import print_function


def read_card_data_from_serial():
    # функция считывания данных с последовательного порта
        data_from_serial = ""
        current_char = ''
        serial_reader = serial.Serial("/dev/ttyUSB0", baudrate=9600)
        while current_char != '\r':
                current_char = serial_reader.read()
                data_from_serial += current_char
        serial_reader.close()
        return data_from_serial


def parse_id_from_card_data(card_data):
    # функция-парсер, возвращающая строку с идентификатор карты или пустую строку в случае неудачи
    try:
        second_block = card_data.split(',')[1]
        return second_block.split()[2]
    except IndexError:
        return ''


def request_permission_for_auth(card_id):
    # функция отправляющая запрос на разрешение аутентификации на сервер
    # и получающую ответ DENY, ALLOW или 'NETWORK_ERROR'
    # (в виде заглушки, с авторизацией по моей карте)
    try:
        arm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        arm_socket.connect((constants.SERVER_HOST, constants.PORT))
        arm_socket.sendall(card_id)
        data = arm_socket.recv(1024)
    except socket.error:
        return 'NETWORK_ERROR'
    finally:
        arm_socket.close()
    return data

data_for_parse = read_card_data_from_serial()
card_id = parse_id_from_card_data(data_for_parse)
print card_id

# TODO - написать функцию, которая авторизует пользователя (или нет)

# TODO - выявить исключения, с которыми программа падает и написать обработчики для них

# TODO - разбить программу на модули, если требуется

# TODO написать unit-тесты под все это дело, если будет время и желание

# TODO - написать описание программы

# TODO - написать комментарии и документацию к программе
