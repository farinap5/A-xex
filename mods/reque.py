from urllib import request
import matplotlib.pyplot as plt
from mods import a_main

def req():


    x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    y = ['0']
    titulo = "Bar Graphs"
    eixox = "requests number"
    eixoy = "code response"
    print('Example: http://example.com')
    ll = input('insert web site: ')
    for l in range(0, 10):
        resp = request.urlopen(ll)

        if resp.code == 200:
            print('\033[1;32m >', resp.code, '\033[0;0m')
            # print ('\033[1;32m [URL is up] \033[1;32m')
            y.append(resp.code)
        else:
            print('', resp.code, '')

    # for z in y:
    # print(z)

    plt.title(titulo)
    plt.xlabel(eixox)
    plt.ylabel(eixoy)

    plt.plot(x, y)
    # plt.legend()
    plt.show()

    input('press enter')
    a_main.a_main()