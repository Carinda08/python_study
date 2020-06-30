import re

def findPhoneNbr():
    print('\nIn Funtion findPhoneNbr:')
    #                     (      0000    )    -       0000     -     0000
    allNbr =re.compile(r'(\()?(\d{3,4})(\))?(\ |-)?(\d{3,4})(\ |-)?(\d{4,5})')

    nbr1 = "my number is 138-1111-1234"
    nbr2 = "my number is 13800012345"
    nbr3 = "my number is 138-000-12345"
    nbr4 = "my number is 138 0000 1234"
    nbr5 = "my home number is (010)1111-1234 and work number is (0532)55678006"
    nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5]

    for line in nbrs:
        mo = allNbr.findall(line)
        if mo is None:
            print("Not Found Phone Number")
        else:
            for nbr in mo:
                print("found number :" + "".join(tuple(nbr)))
#?:
def pattern1():
    print('\nIn Funtion pattern1:')
    s='goodie is good, and goodbye is good too'

    good=re.compile(r'good(?:ie|bye)')
    mo = good.findall(s)
    print('?: goodie and goodbye')
    print(mo)

    good=re.compile(r'good(ie|bye)')
    mo = good.findall(s)
    print('None ie and bye start with good')
    print(mo)

    good=re.compile(r'(good)(ie|bye)')
    mo = good.findall(s)
    print('() goodie and goodbye')
    print(mo)

    good=re.compile(r'good(?!ie|bye)')
    mo = good.findall(s)
    print('?! good without ie or bye')
    print(mo)


def findIp():
    print('\nIn Funtion findIp:')
    s=' 192.137.1.336  192.168.1.137.123  192.168.1.138 '
    reIp = re.findall(r'(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])',s)
    print(reIp)

if __name__ == '__main__':
    findPhoneNbr()
    findIp()
    pattern1()
