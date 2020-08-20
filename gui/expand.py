#!/usr/bin/env python3
# -*- coding=utf8 -*-
"""
# Author: Carinda
# Created Time : 2020/8/19 11:00:47
# File Name: expand.py
# Description:
"""


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:  %(message)s')

from tkinter import *

win = Frame()
win.pack(expand=YES, fill=BOTH)
Button(win, text='111').pack(side=LEFT, fill=Y)
Label(win, text='ass').pack(side=TOP)
Button(win, text='222').pack(side=RIGHT, expand=YES, fill=BOTH)
win.mainloop()
