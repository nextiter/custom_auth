#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# arm_auth.py
#
# Программа ожидает, когда будет приложена смарт-карта
# считывает с неё данные
# парсит ID карты
# отправляет ИД на сервер
# получает ответ ALLOW или DENY
# при получении ALLOW авторизует пользователя под учетной записью user1
# 11.08.2016
# author S.Ivakhov <nextiter@gmail.com>
#

import socket
import serial
import time

SERVER_HOST = "192.168.0.37"
CLIENT_HOST = "192.168.0.244"
PORT = 9009
USER = 'user1'


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
        arm_socket.connect((SERVER_HOST, PORT))
        arm_socket.sendall(card_id.encode('utf-8'))
        data = arm_socket.recv(1024)
    except socket.error:
        return 'NETWORK_ERROR'
    finally:
        arm_socket.close()
    return data


def pam_sm_authenticate(pamh, flags, argv):
    # пользователь, под которым авторизуемся
    pamh.user = 'user1'
    # считываем данные с карты
    card_data = read_card_data_from_serial()
    # парсим ИД
    id_for_check = parse_id_from_card_data(card_data)
    if request_permission_for_auth(id_for_check) == 'ALLOW':
        return pamh.PAM_SUCCESS
    else:
        return pamh.PAM_USER_UNKNOWN


def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_acct_mgmt(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_open_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_chauthtok(pamh, flags, argv):
    return pamh.PAM_SUCCESS
