#!/usr/bin/env python3
# -*- coding=utf8 -*-
"""
# Author: Carinda
# Created Time : 2020/8/20 10:23:04
# File Name: demoDlg.py
# Description:
"""


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:  %(message)s')

from tkinter import *
from dialogTable import demos

class DlgDemo(Frame):
    def __init__(self, parent=None, **configs):
        Frame.__init__(self, parent, **configs)
        self.pack()
        Label(self, text='Basic Demos').pack()
        for(key, cmd) in demos.items():
            fuc = (lambda handler=self.printRet, name=key: handler(name))
            # Button(self, text=key, command=cmd).pack(side=TOP, fill=BOTH)
            Button(self, text=key, command=fuc).pack(side=TOP, fill=BOTH)

    def printRet(self, name):
        print(name, 'ret=>', demos[name]())

if __name__ == '__main__':
    DlgDemo().mainloop()
