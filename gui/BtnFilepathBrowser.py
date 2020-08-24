#!/usr/bin/env python3
# -*- coding=utf8 -*-
"""
# Author: Carinda
# Created Time : 2020/8/17 15:47:02
# File Name: BtnFilepathBrowser.py
# Description:
"""


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:  %(message)s')

from tkinter import *
from tkinter.filedialog import askdirectory

class ButtonFilepathBrowser(Button):
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs)
        self.pack()
        # self.config(fg='yellow', bg='black', font=('courier', 12), relief=RAISED, bd=5)
        self.config(text = "Browser")
        self.config(command=self.callback)
        ButtonFilepathBrowser.path = StringVar()
        ButtonFilepathBrowser.path.set('.')

    def callback(self):
        path = (askdirectory())
        ButtonFilepathBrowser.path.set(path)
        logging.debug("self.path = %s", ButtonFilepathBrowser.path.get())

    def setPath(self, path):
        ButtonFilepathBrowser.path = path

if __name__ == "__main__":
    ButtonFilepathBrowser().mainloop()
