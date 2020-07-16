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



    linha()
    print("Ip Address:      ",ipaddr)
    print("Service:         ",domwho.name)
    print("Expiration Date: ",domwho.expiration_date)
    print("Creation Date:   ",domwho.creation_date)
    print("Last Update:     ",domwho.last_updated)
    #print("Owner:           ",domwho.owner)
    print("Regist:          ",domwho.registrar)
    print("Status:          ",domwho.status)
    print("Server:          ",domwho.name_servers)

    try:
        linha()
        print("\033[1;32mHeaders Response\033[0;0m")
        domht = "http://"+ dom
        donthh = "http://api.hackertarget.com/httpheaders/?q=" + dom
        print(requests.get(donthh).text)
    except:
        pass

    f = request.urlopen(domht)
    print(f.getcode())
    print(f.info())

    linha()
    print("\033[1;32mRedirection\033[0;0m")
    response = requests.get(domht)
    if response.is_redirect == False:
        print("No Redirection")
    else:
        print("Web Site Redirecting")

    try:
        linha()
        print("\033[1;32mDNS Lookup\033[0;0m")
        print(requests.get("https://api.hackertarget.com/mtr/?q=" + dom).text)
    except:
        pass
    try:
        linha()
        print("\033[1;32mHost Search\033[0;0m")
        print(requests.get("https://api.hackertarget.com/hostsearch/?q=" + dom).text)
    except:
        pass
    try:
        linha()
        print("\033[1;32mFind Shared DNS\033[0;0m")
        print(requests.get("https://api.hackertarget.com/findshareddns/?q=" + dom).text)
    except:
        pass
    input("press enter")
    a_main.a_main()

