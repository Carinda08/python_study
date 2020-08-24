#!/usr/bin/env python3
# -*- coding=utf8 -*-
"""
# Author: Carinda
# Created Time : 2020/8/17 15:33:39
# File Name: FrameFilePath.py
# Description:
"""


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:  %(message)s')

from tkinter import *
from BtnFilepathBrowser import ButtonFilepathBrowser

class FrameFilepath(Frame):
    def __init__(self, path='.', parent=None):
        Frame.__init__(self, parent)
        self.path = StringVar()
        self.path.set(path)
        self.pack(expand=YES, fill=BOTH)
        self.initWidght()

    def initWidght(self):
        lbl = Label(self, text='File Path')
        lbl.pack(side=LEFT)
        # lbl.config(fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=5)
        ent = Entry(self)
        ent.pack(side=LEFT, expand=YES, fill=X)
        ent.config(textvariable=self.path)
        btn = ButtonFilepathBrowser(self)
        btn.pack(side=LEFT)
        btn.setPath(self.path)

    def updateVar(self):
        self.path.set(btn.path)

if __name__ == '__main__':
    FrameFilepath().mainloop()
