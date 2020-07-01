import re

phnRgx = re.compile(r'''
                    (\()?               # (
                    (\d{3,4})           # area number
                    (\))?               # )
                    (\ |-)?             # ' ' or '-'
                    (\d{3,4})           # middle number
                    (\ |-)?             # ' ' or '-'
                    (\d{4,5})           # last number
                    '''
                    , re.VERBOSE
                    )

def findPhoneNbr():
    print('\nIn Funtion findPhoneNbr:')

    nbr1 = "my number is 138-1111-1234"
    nbr2 = "my number is 13800012345"
    nbr3 = "my number is 138-000-12345"
    nbr4 = "my number is 138 0000 1234"
    nbr5 = "my home number is (010)1111-1234 and work number is (0532)55678006"
    nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5]

    for line in nbrs:
        mo = phnRgx.findall(line)
        if mo is None:
            print("Not Found Phone Number")
        else:
            for nbr in mo:
                print("found number :" + "".join(tuple(nbr)))

if __name__ == '__main__':
    findPhoneNbr()
