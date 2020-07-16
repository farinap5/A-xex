import socket
import platform


plat = platform.system()
clat = platform.release()
sac = platform.version()
def ipdist():
    try:
        hostName = socket.gethostname()

        ipaddr = socket.gethostbyname(hostName)


        print("  Host Name: ",'\033[1;32m',plat,'',hostName,'',clat,'\033[0;0m')
        print("  IP Address:",'\033[1;32m',ipaddr,'\033[0;0m')
    except:
        print('[\033[1;31m!\033[0;0m]- No Dist')
        print('[\033[1;31m!\033[0;0m]- No IP')
