from urllib import request
import subprocess
import requests

def cheknet():
    try:
        url = "http://google.com.br"
        resp = request.urlopen(url)
        print('  [\033[1;32mOK\033[0;0m]-Internet')
    except:

        print('  [\033[1;31m!\033[0;0m]- No connection.')
        print('  Are you sure you want to continue?')
        print('  The modules will not work.')
        z = input('  [Y]es/[N]o >')
        list = ['N', 'n', 'no', 'No']
        if z in list:
            exit()
        else:
            print('\n')
            pass



def checkv():
    try:
        at_vesion = 1.4
        url = "https://raw.githubusercontent.com/farinap5/A-xex/master/mods/version.txt"

        try:
            r = requests.get(url)
            vrs = float(r.text)

            if vrs == at_vesion:
                print("  [\033[1;32mOK\033[0;0m]-Version.\n")
            else:
                print("  [\033[1;31m!\033[0;0m]-There is a newer version available",vrs)
                print("\n")


        except:
            pass
    except:
        pass




def seenet():
    try:
        results = subprocess.check_output(["netsh", "wlan", "show", "network"])
        results = results.decode("ascii")
        results = results.replace("\r", "")
        ls = results.split("\n")
        ls = ls[4:]
        ssids = []
        x = 0
        while x < len(ls):
            if x % 5 == 0:
                ssids.append(ls[x])
            x += 1
        print(ssids)
    except:
        print('[!]-Error')
