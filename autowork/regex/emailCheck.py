import re

emailRgx = re.compile(r'''
                       ([a-zA-Z0-9._%+-]+)    #username
                       (@)                    #'@'
                       ([a-zA-Z0-9._%+-]+)    #domain name
                       (\.[a-zA-Z]{2,4})+     #'cn','com',etc
                       '''
                       , re.VERBOSE)

def findEmail():
    print("\n In Function findEmail")

    nbr1 = "my email is ddd0998@qq.com"
    nbr2 = "my email is ddd.0998@qq.com.cn"
    nbr3 = "my email is ddd_0998@icloud.com"
    nbr4 = "my email is ddd-0998@icloud.com"
    nbr5 = "my home email is wrong*@qdaoe.cn and work email are wrong#qdaoe.cn and wrong123@qdaoe.qdaoe"
    nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5]

    for line in nbrs:
        mo = emailRgx.findall(line)
        if mo is None:
            print("Not Found Phone Email")
        else:
            for nbr in mo:
                print("found email :" + "".join(tuple(nbr)))

if __name__ == '__main__':
    findEmail()
