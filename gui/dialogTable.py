#!/usr/bin/env python3
# -*- coding=utf8 -*-
"""
# Author: Carinda
# Created Time : 2020/8/20 10:18:49
# File Name: dialogTable.py
# Description:
"""


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:  %(message)s')

from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

demos  ={
        'Open': askopenfilename,
        'Color': askcolor,
        'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
        'Error': lambda: showerror('Error!', "What do you want!"),
        'Input': lambda: askfloat('Entry', 'Enter you phone number'),
        }
