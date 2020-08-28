import socket
import whois
from ipwhois import IPWhois
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
        print("  Would you like to continue?")
        x = input("   y/n > ")
        if x == ("n","N","no","No"):
            a_main.a_main()
        else:
            pass

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
    print("  Redirecting:           ",red.is_redirect)
    print("  Redirecting Permanent: ",red.is_permanent_redirect)
    print("  Encoding:              ",red.apparent_encoding)
    print("  Next:                  ",red.next)

    zin = requests.get(domht).text
    if "<form" and "</form>" in zin:
        print("  Form Found")
    else:
        pass
    linha()
    obj = IPWhois(ipaddr)
    job = obj.lookup_whois()
    print('  \033[1;32mWhois IP\033[0;0m')
    print(' Query:           ', job["query"])
    print(' Nir:             ', job["nir"])
    print(' Asn Registry:    ', job["asn_registry"])
    print(' Asn:             ', job["asn"])
    print(' Asn Cidr:        ', job["asn_cidr"])
    print(' Asn Country Code:', job["asn_country_code"])
    print(' Asn Date:        ', job["asn_date"])
    print(' Raw:             ', job["raw"])
    print(' Referral:        ', job["referral"])
    print(' Raw Referral:    ', job["raw_referral"])

    print('  \033[1;32mNets\033[0;0m')
    for k in job["nets"]:
        print(' Cidr:        ', k["cidr"])
        print(' Name:        ', k["name"])
        print(' Handle:      ', k["handle"])
        print(' Range:       ', k["range"])
        print(' Description: ', k["description"])
        print(' Country:     ', k["country"])
        print(' State:       ', k["state"])
        print(' City:        ', k["city"])
        print(' Address:     ', k["address"])
        print(' Postal Code: ', k["postal_code"])
        print(' Created:     ', k["created"])
        print(' Updated:     ', k["updated"])


    input("press enter")
    a_main.a_main()

