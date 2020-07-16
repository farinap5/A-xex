from mods import a_main
import dns.resolver
import time
import requests
from urllib import request
import re


def dnsbrute():
    #os.system('clear')
    print('  DNS finder with Brute Force')
    print('  Example: example.com')

    try:
        dominio = input('  Set web site: ')
    except:
        dominio = 'example.com'

    print('  [ok]',dominio)
    print('  Recomended - dnswl.txt')

    try:
        lista = input('  Set wordlist: ')
    except:
        print('  invalid')
        dnsbrute()

    print('  [ok]',lista)

    # abre a wordlist
    try:
        arquivo = open(lista)
        linhas = arquivo.read().splitlines()
    except:
        print("   The file is not valid.")
        time.sleep(0,3)
        dnsbrute()

    # para cada linha da wordlist testa o dns
    for linha in linhas:
        subdominio = linha + '.' + dominio
        try:
            respostas = dns.resolver.query(subdominio, 'a')
            for resultado in respostas:
                print('  Found------------------------')
                print('  [ok]', subdominio, resultado)
        except:
           pass
    input('press enter')
    a_main.a_main()

def repfind():
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chome/51.0.2704.103 Safari/537.36'}

    print('  Directory Brute Finder')
    try:
        print('  Set Web Site, example: http://example.com')
        url = input('  > ')

        try:
            z = requests.get(url)
            if z.status_code == 200:
                print('  [\033[1;32mOK\033[0;0m]-',url,'\n')
        except:
            print('  [\033[1;31m!\033[0;0m]-Something was wrong.\n')
            time.sleep(1)
            repfind()

        print('  Set Path to the WordList')
        print('  Recomended- direc.txt ')
        arq = input('  >> ')

        arqui = open(arq)
        lin = arqui.readlines()
        for linha in lin:

            uzs = url +"/"+ linha
            try:
                resp = request.urlopen(uzs)
                print('  [\033[1;32mOK\033[0;0m]-',uzs)
            except:
                pass
        print('  [\033[1;32m!\033[0;0m]- Done')
        input('press enter')
        a_main.a_main()





    except:
        print('  [\033[1;31m!\033[0;0m]-Something was wrong.\n')
        time.sleep(1)
        repfind()


def spider():
    print('  Find urls using spiders\n')
    print('  Set Web page, example: http://example.com')
    urll = input('  > ')
    try:
        z = requests.get(urll)
        if z.status_code == 200:
            print('  [\033[1;32mOK\033[0;0m]-', urll, '\n')
    except:
        print('  [\033[1;31m!\033[0;0m]-Something was wrong.\n')
        time.sleep(1)
        spider()

    html = requests.get(urll).text

    urls = re.findall('(?<=href=["\'])https?://.+?(?=["\'])', html)
    kato = 0
    for url in urls:
        kato = kato + 1
        print(kato,'  [\033[1;32mOK\033[0;0m]-',url)

    input('  press enter')
    a_main.a_main()




