import re

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


if __name__ == '__main__':
    pattern1()
