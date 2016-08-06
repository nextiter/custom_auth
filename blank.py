#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Заготовка для программы
# Все блоки комментариев начианющихся с TODO - необходимо заменить на работающие части программы

import serial
import socket
import constants
#from __future__ import print_function

# функция считывания данных с последовательного порта


def read_card_data_from_serial():
        data_from_serial = ""
        current_char = ''
        serial_reader = serial.Serial("/dev/ttyUSB0", baudrate=9600)
        while current_char != '\r':
                current_char = serial_reader.read()
                data_from_serial += current_char
        serial_reader.close()
        return data_from_serial

# TODO - написать функцию-парсер, возвращающую идентификатор карты


def parse_id_from_card_data(card_data):
    try:
        second_block = card_data.split(',')[1]
    except IndexError:
        return 0
    try:
        return int(second_block.split()[2])
    except ValueError:
        return 0

# TODO - написать функцию отправляющую запрос об идентификаторе на сервер и получающую ответ
#  (в виде заглушки, с авторизацией по моей карте)

# TODO - написать функцию, которая авторизует пользователя (или нет)

# TODO - выявить исключения, с которыми программа падает и написать обработчики для них

# TODO - разбить программу на модули, если требуется

# TODO написать unit-тесты под все это дело, если будет время и желание

# TODO - написать описание программы

# TODO - написать комментарии и документацию к программе
