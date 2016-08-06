#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# custom_linux_auth.py
#
# Момент истины: если сейчас авторизация пройдет успешно, значит программа практически готова.
# 19.07.2016
# author S.Ivakhov <nextiter@gmail.com>
#

import constants
import blank


def pam_sm_authenticate(pamh, flags, argv):
    pamh.user = constants.USER
    card_id = blank.parse_id_from_card_data('Wiegand Hex = 7D3257, DECIMAL = 8204887, Type W26')
    if blank.request_permission_for_auth(card_id):
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
