import re

def findIp():
    print('\nIn Funtion findIp:')
    s=' 192.137.1.336  192.168.1.137.123  192.168.1.138 '
    reIp = re.findall(r'(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])',s)
    print(reIp)

if __name__ == '__main__':
    findIp()
