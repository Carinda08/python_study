#!/usr/bin/env python3
# -*- coding=utf8 -*-
"""
# Author: Carinda
# Created Time : Thu 20 Aug 2020 06:14:04 PM PDT
# File Name: Entry.py
# Description:
"""


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:  %(message)s')


from tkinter import *

fields = {'Name':'Bob', 'Job':'Car engineer', 'Pay':'10000'}

def fetch():
    print('Input is : "%s"' % ent.get())

def fetchall(entries):
    for ent in entries:
        print('Input is : "%s"' % ent.get())

def ask():
    popup = Toplevel()
    ents = makeform(popup, fields)
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()

def makeform(root, fields):
    entries = []
    for field, text in fields.items():
        row = Frame(root)
        lab = Label(row, width=5, text=field)
        ent = Entry(row)
        var = StringVar()
        var.set(text)
        ent.config(textvariable=var)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(var)

    root.bind('<Return>', (lambda event: fetchall(entries))) # Return has a parameter 'event'
    Button(root, text='Fetch', command=(lambda: fetchall(entries))).pack(side=LEFT)


def makeEnt(root):
    ent = Entry(root)
    ent.insert(0, 'Type word here')
    ent.pack(side=TOP, fill=X)
    ent.bind('<Return>', (lambda event: fetch())) # Return has a parameter 'event'


    ent.focus()
    btn = Button(root, text='Fetch', command=fetch)
    btn.pack(side=LEFT)

# start function
def singleEnt():
    makeEnt(root)

def formEnt():
    makeform(root, fields)

def askEnt():
    Button(root, text="Start ask", command=ask).pack()

if __name__ == '__main__':
    root = Tk()

    # singleEnt()
    # formEnt()
    askEnt()

    root.mainloop()
