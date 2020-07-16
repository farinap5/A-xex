from mods import a_main
import time
import os

def about():

    print ('   This tool was made to help all pentesters, making those tests easier')
    print ('        and faster, we puted those  most  importants tools in one.')
    print ('      You use this tool for what you want to do, we do not encourage')
    print ('         the bad uses, we are not responsible for malicious use!')
    print ('                           !You own your acts!')


    con = [5,4,3,2,1,0]
    for n in con:
        print(' ', n, end="\r")
        time.sleep(1)

    try:
        os.system('firefox https://farinap5.github.io/axex/axex/')
        exit("[ok]-Firefox Found.")

    except:
        print('[!]-No firefox found. Enter https://farinap5.github.io/axex/axex/')
        input("press enter")
        a_main.a_main()