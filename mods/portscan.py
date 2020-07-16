from mods import a_main
import socket


def portscansim():
    print ('  A-xex Port Scaner- Scan The Principal \n')
    ip = input('  Set Target: ')
    ports = [21, 22, 23, 25, 80, 443, 445, 3306, 2121, 5555, 8080]


    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)

        code = client.connect_ex((ip, port))

        if code == 0:
            print(str(port) + (' \033[1;32m -> Opened Port!\033[0;0m '))
        else:
            print(str(port) + (' \033[1;31m -> Closed Port!\033[0;0m '))
    print('  Finished scan')
    input('Press Enter')
    a_main.a_main()

def  portscanbrange():
    print('  A-xex Port Scaner- Big Range')
    print('  It Might Took A Long Time!\n')
    ip = input('  Insert an ip or an address: ')
    ports = range(65535)


    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)

        code = client.connect_ex((ip, port))

        if code == 0:
            print (str(port) + (' \033[1;32m -> Opened Port!\033[0;0m '))
        else:
            print(str(port) + (' \033[1;31m -> Closed Port!\033[0;0m '))
    print('  Finished scan')
    input('Press Enter')
    a_main.a_main()


def portscanch():
    listports = []
    print('  Port scanner- Scans Specific Ports')
    try:
        ip = input('  set ip addres> ')
        #ip = "192.168.15.167"
    except:
        print('  set correct ip or domain')
        portscanch()
    print('  example how to use: 21 22 80 443 5555')
    print('  the maximum is five\n')

    try:
        listports = input('  Insert Port: ').split(" ")
    except:
        print('set ports.')
        portscanch()

    try:
        p = int(listports[0])
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip, p))
        if code == 0:
            print(str(p) + (' \033[1;32m -> Opened Port!\033[0;0m '))
        else:
            print(str(p) + (' \033[1;31m -> Closed Port!\033[0;0m '))
        pass

        po = int(listports[1])
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip, po))
        if code == 0:
            print(str(po) + (' \033[1;32m -> Opened Port!\033[0;0m '))
        else:
            print(str(po) + (' \033[1;31m -> Closed Port!\033[0;0m '))
        pass

        por = int(listports[2])
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip, por))
        if code == 0:
            print(str(por) + (' \033[1;32m -> Opened Port!\033[0;0m '))
        else:
            print(str(por) + (' \033[1;31m -> Closed Port!\033[0;0m '))
        pass

        port = int(listports[3])
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip, port))
        if code == 0:
            print(str(port) + (' \033[1;32m -> Opened Port!\033[0;0m '))
        else:
            print(str(port) + (' \033[1;31m -> Closed Port!\033[0;0m '))
        pass

        ports = int(listports[4])
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip, ports))
        if code == 0:
            print(str(ports) + (' \033[1;32m -> Opened Port!\033[0;0m '))
        else:
            print(str(ports) + (' \033[1;31m -> Closed Port!\033[0;0m '))
        pass
    except:
        pass

    print('  Finished scan')
    input('Press Enter')
    a_main.a_main()

