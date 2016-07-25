#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	custom_linux_auth.py
#	
#	Модуль для кастомной авторизации в linux
#	Использует систему PAM (Pluggable Authentication Modules) и библиотеку libpam-python
#	Авторизует двух пользователей root и sam, меняя их местами, т.е.
#	если необходимо авторизоваться под учетной записью sam - необходимо вводить root
#	и наоборот.
#	Также авторизация будет успешна только в случае если текущая минута четная.
#	Пароль не запрашивается.
#	
#	Модуль создан для обзора возможностей библиотеки libpam-python и ее оценки
#	для реализации решений реальных задач
#
#	19.07.2016
#	author S.Ivakhov <nextiter@gmail.com>
#	


def check_access_by_minutes():
	from datetime import datetime
	now_time = datetime.now()
	minutes = now_time.minute
	if minutes % 2 == 0:
		return True
	else:
		return False


def pam_sm_authenticate(pamh, flags, argv):
	# Get the user name.
	try:
		username = pamh.get_user()
	except pamh.exception:
		username = None
	if username == None:
		return pamh.PAM_USER_UNKNOWN
	elif username == "sam":
		pamh.user = "root"
		if check_access_by_minutes():
			return pamh.PAM_SUCCESS
		else:
			return pamh.PAM_USER_UNKNOWN
			
	elif username == "root":
		pamh.user = "sam"
		if check_access_by_minutes():
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
