import requests
import re
from mods import a_main

def sqliscan():
    try:
        print('  SQLI Scan')
        url = input('  set URL> ')
    except:
        print('  [\033[1;31m!\033[0;0m]- Something was wrong.')
        input('press enter')
        sqliscan()
    #colocar essa barra na url para n acusar sendo uma aspa do codigo

    padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)',url)

    inject = padrao.groups()[0] + '\''

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