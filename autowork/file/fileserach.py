import shutil, os, sys
import logging

#logging.basicConfig(level=logging.DEBUG,
#        format='%(asctime)s:  %(message)s')

logging.debug('head')
sdir = '.'
sext = ''

allFileList = []

def runsearch():
    initPara()
    for floder, subfolders, filenames in os.walk(sdir):
        for filename in filenames:
            if (checkext(filename)):
                allFileList.append(floder+"/"+filename)

def checkext(fname):
    if sext == '':
        logging.debug(sext)
        return True

    ls = fname.split('.')
    # if ls[-1] == sext:
    #     logging.debug('true')
    #     return True
    # else:
    #     logging.debug('FALSE')
    #     return False
    return True if ls[-1] == sext else False

def initPara():
    if len(sys.argv) > 1:
        global sdir
        sdir = sys.argv[1]
        logging.debug("path = " + sdir)

    if len(sys.argv) > 2:
        global sext
        sext = sys.argv[2]
        logging.debug("ext = " + sext)


if __name__ == '__main__':
    runsearch()
    print(allFileList)
