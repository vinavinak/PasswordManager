#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Kana Kunikata
# Created Date: 02/04/2022
# version ='1.0'
# ---------------------------------------------------------------------------

""" Testing Password Manager """

from password_manager_main import PasswordManager, main
import pytest

async def _start_app(app):
#def _start_app(app):
        app.mainloop()

def test_startup():
    #root = Tk()
    app = main()
    _start_app(app)
    title = app.winfo_toplevel().title()
    expected = 'Password Manager'
    assert title == expected


def test_always_passes():
    assert True
