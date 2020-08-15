import socket
import whois
from urllib import request
import requests
from mods import a_main

def descoverdom():
    def linha():
        print('\033[1;32m------------------------------------\033[0;0m')

    linha()
    print('  Info Gether from Dominio')
    print('  Set A Host: example.com')
    try:
        dom = input('  >> ')
    except:
        print('Something was wrong')
    #dom = "google.com"
    ipaddr = socket.gethostbyname(dom)

    domwho = whois.query(dom)

    domht = "http://" + dom

    linha()

    cf = requests.get(domht).text
    c1 = '<div class="cf-browser-verification cf-im-under-attack">'
    c2 = 'Checking your browser before accessing'
    c3 = 'Please enable Cookies and reload the page'
    c4 = 'DDoS protection by'

    if c1 and c2 and c3 and c4 in cf:
        print("  Cloud Flare: True")
        print("  Would you like to continue")
    else:
        print("  No Cloud Flare")

    print("  Ip Address:      ",ipaddr)
    print("  Service:         ",domwho.name)
    print("  Expiration Date: ",domwho.expiration_date)
    print("  Creation Date:   ",domwho.creation_date)
    print("  Last Update:     ",domwho.last_updated)
    print("  Name Servers:    ",domwho.name_servers)
    print("  Register:        ",domwho.registrar)

    linha()

    f = request.urlopen(domht)
    print("  Code: ",f.getcode())
    print(f.info())

    linha()

    red = requests.get(domht)
    print("Redirecting:           ",red.is_redirect)
    print("Redirecting Permanent: ",red.is_permanent_redirect)
    print("Encoding:              ",red.apparent_encoding)
    print("Next:                  ",red.next)

    zin = requests.get(domht).text
    if "<form" and "</form>" in zin:
        print("Form Found")
    else:
        pass




    input("press enter")
    a_main.a_main()

