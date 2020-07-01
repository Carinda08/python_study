'''
Finds phone number and email from clipboard
'''

import pyperclip
import sys

#sys.path.append("p:\code\python\python_study\autowork\regex")

import emailCheck
import phonenbrCheck

def runCheck():
    print('\n In Function runCheck')

    text = str(pyperclip.paste())
    print(text)
    matchs = []

    # find phone number
    for g in phonenbrCheck.phnRgx.findall(text):
        phoneNbr = '-'.join([g[1], g[4], g[6]])
        matchs.append(phoneNbr)

    # find email
    for e in emailCheck.emailRgx.findall(text):
        email = "".join(tuple(e))
        matchs.append(email)

    print(matchs)

    # output to clipboard
    if len(matchs) > 0:
        pyperclip.copy("\n".join(matchs))
        print("Clipboard copyed: ")
        print("\n".join(matchs))
    else:
        print("No phone number or email found.")

if __name__ == "__main__":
    runCheck()
