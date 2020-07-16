import socket
from ipwhois import IPWhois
from urllib import request
import ipwhois
import requests
from mods import a_main

def domip():
    def linha():
        print('\033[1;32m------------------------------------\033[0;0m')


    linha()
    print("  Ip Scan InfoGet")
    ip = input('  Set Host Ip> ')

    print("IP Address: ",ip)

    obj = IPWhois(ip)
    job = obj.lookup_whois()
    print('  \033[1;32mWhois IP\033[0;0m')
    print(' Query:           ',job["query"])
    print(' Nir:             ',job["nir"])
    print(' Asn Registry:    ',job["asn_registry"])
    print(' Asn:             ',job["asn"])
    print(' Asn Cidr:        ',job["asn_cidr"])
    print(' Asn Country Code:',job["asn_country_code"])
    print(' Asn Date:        ',job["asn_date"])
    print(' Raw:             ',job["raw"])
    print(' Referral:        ',job["referral"])
    print(' Raw Referral:    ',job["raw_referral"])

    print('  \033[1;32mNets\033[0;0m')
    for k in job["nets"]:
        print(' Cidr:        ',k["cidr"])
        print(' Name:        ',k["name"])
        print(' Handle:      ',k["handle"])
        print(' Range:       ',k["range"])
        print(' Description: ',k["description"])
        print(' Country:     ',k["country"])
        print(' State:       ',k["state"])
        print(' City:        ',k["city"])
        print(' Address:     ',k["address"])
        print(' Postal Code: ',k["postal_code"])
        print(' Created:     ',k["created"])
        print(' Updated:     ',k["updated"])

        for e in k["emails"]:
            print('  ',e)



    #linha()
    #print(obj.lookup_rdap())

    linha()
    print('\033[1;32mReverse DNS\033[0;0m')
    print(requests.get("https://api.hackertarget.com/reversedns/?q=" + ip).text)

    linha()
    print('\033[1;32mGeo IP\033[0;0m')
    print(requests.get("https://api.hackertarget.com/geoip/?q=" + ip).text)

    linha()
    print('\033[1;32mReverse ip Lookup\033[0;0m')
    print(requests.get("https://api.hackertarget.com/reverseiplookup/?q=" + ip).text)

    linha()
    print('\033[1;32mTrace Route\033[0;0m')
    print(requests.get("https://api.hackertarget.com/mtr/?q=" + ip).text)
    input("press enter")
    a_main.a_main()



