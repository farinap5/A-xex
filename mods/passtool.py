import random
from mods import a_main


def passgen():
    s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890"
    try:
        print('  Set Password Length')
        passlen = int(input('  >> '))
        password = "".join(random.sample(s,passlen))
        print('  >> ', password, '\n')
        input('press enter')
        a_main
    except:
        print('  [!] - Error')
        input('  press enter')
        passgen()
