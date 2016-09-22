#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#
# db_worker.py
# Реализован интерфейс для работы с базой данных СКУД
# FireBird, из которой берутся данные для авторизаци пользователя АРМ
#
# 20.09.2016
# author S.Ivakhov <nextiter@gmail.com>

import fdb
import constants

class DBWorker:
    def __init__(self):
        try:
            self.db_connect = fdb.connect(user=constants.DB_USER,
                                          password=constants.DB_PASSWORD,
                                          host=constants.DB_HOST,
                                          database=constants.DATABASE
                                          )
        except fdb.fbcore.DatabaseError:
            print "Database Error"
            self.db_connect = False

    def get_emloyee_info(self, card_id):
        try:
            curs = self.db_connect.cursor()
            result_query = curs.execute("SELECT N, CODE, NUMBER_, NUM_KD, F_NAME, S_NAME, M_NAME, LEVEL_KD FROM CLITAB WHERE CODE=" + card_id)
            if result_query:
                first_row = result_query.fetchall()[0]
                employee = {
                    'db_id': first_row[0],
                    'dec_card_id': first_row[1],
                    'tabel_number': first_row[2],
                    'hex_card_id': first_row[3],
                    'first_name': first_row[4].decode('cp1251'),
                    'second_name': first_row[5].decode('cp1251'),
                    'midle_name': first_row[6].decode('cp1251'),
                    'level': int(first_row[7]),
                }
                return employee

        except IndexError:
            print"Empty response from DB"
        except AttributeError:
            print "Not connected."

        return False

