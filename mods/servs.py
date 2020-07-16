import subprocess
from mods import a_main


def sftps():
    print('  xterm ftp')
    c = ['xterm']
    l = input(' port> ')
    if len(l) >= 1:
        p = '-p ' + l
        print(' [+] arg port ', p)
        z = 'python -m pyftpdlib ' + p + ' && exit; exec $SHELL'
    else:
        p = '-p ' + '2121'
        print(' [+] defalt port 2121')
        z = 'python -m pyftpdlib ' + p + ' && exit; exec $SHELL'

    print(z)

    c.extend(['-e', 'bash', '-c', z])
    subprocess.Popen(c, stdout=subprocess.PIPE)
    input('press enter to return')
    a_main.a_main()

def shttps():
    print('  xterm HTTP')
    c = ['xterm']
    l = input(' port> ')
    if len(l) >= 1:
        p = l
        print(' [+] arg port ', p)
        z = 'python -m SimpleHTTPServer ' + p + ' && exit; exec $SHELL'
    else:
        p = '8000'
        print(' [+] defalt port 8000')
        z = 'python -m SimpleHTTPServer ' + p + ' && exit; exec $SHELL'

    print(z)

    c.extend(['-e', 'bash', '-c', z])
    subprocess.Popen(c, stdout=subprocess.PIPE)
    input('press enter to return')
    a_main.a_main()