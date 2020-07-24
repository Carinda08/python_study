#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Carinda
# Created Time : 2020年07月22日 星期三 14时42分12秒
# File Name: filesearchByName.py
# Description:
"""


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:  %(message)s')


import shutil, os, sys

'''
search all files in the path, and list them
para1 path: search path, default='.'
para2 name: key word in filename, all if null
'''

sdir = '.'
sname = ''

allFileList = []

def runsearch():
    initPara()
    for floder, subfolders, filenames in os.walk(sdir):
        for filename in filenames:
            if (checkname(filename)):
                allFileList.append(floder+"/"+filename)

def checkname(fname):
    if sname == '':
        logging.debug(sname)
        return True

    ls = fname.split('.')
    # if ls[-1] == sname:
    #     logging.debug('true')
    #     return True
    # else:
    #     logging.debug('FALSE')
    #     return False
    return True if ls[-1] == sname else False

def initPara():
    if len(sys.argv) > 1:
        global sdir
        sdir = sys.argv[1]
        logging.debug("path = " + sdir)

    if len(sys.argv) > 2:
        global sname
        sname = sys.argv[2]
        logging.debug("name = " + sname)


if __name__ == '__main__':
    runsearch()
    print(allFileList)
