# All modules to be used across the program funcionalitys
import os
from mods import alogo
from mods import ls
from mods import ipdist
from mods import cheknet
from mods import help
from mods import portscan
from mods import email
from mods import servs
from mods import reque
from mods import repfind
from mods import stress
from mods import passtool
from mods import console
from mods import listener
from mods import vuln
from mods import descoverdom
from mods import descoverip
from mods import hashtool


def a_main():
    alogo.logo()
    ipdist.ipdist()
    cheknet.cheknet()
    cheknet.checkv()

    ls.list1()
    print('\n')
    try:
        es = int(input('  >> '))

        if es == 0:
            alogo.logo()
            help.about()

        if es == 1:
            print('   \033[1;32mPort Scanner\033[0;0m')
            ls.portscanner()
            lsn = int(input('  >> '))
            if lsn == 1:
                portscan.portscansim()
            if lsn == 2:
                portscan.portscanbrange()
            if lsn == 3:
                portscan.portscanch()
            else:
                a_main()

        if es == 2:
            print('   \033[1;32mE-mail Tools\033[0;0m')
            ls.mail()
            lsm = int(input('  >> '))
            if lsm == 1:
                email.sendmailmenssage()
            if lsm == 2:
                print('soon')
                a_main()
            else:
                a_main()

        if es == 3:
            print('   \033[1;32mServers\033[0;0m')
            ls.server()
            lss = int(input('  >> '))
            if lss == 1:
                servs.sftps()
            if lss == 2:
                servs.shttps()
            else:
                a_main()

        if es == 4:
            reque.req()

        if es == 5:
            print('   \033[1;32mWeb Analysis\033[0;0m')
            ls.VulnWeb()
            lsr = int(input('  >> '))
            if lsr == 1:
                repfind.dnsbrute()
            if lsr == 2:
                repfind.repfind()
            if lsr == 3:
                repfind.spider()
            if lsr == 4:
                vuln.sqliscan()
            if lsr == 5:
                descoverdom.descoverdom()
            if lsr == 6:
                descoverip.domip()
            if lsr == 7:
                vuln.xssscan()
            else:
                a_main()

        if es == 6:
            print('   \033[1;32mStress Testing\033[0;0m')
            ls.strss()
            lst = int(input('  >> '))
            if lst == 1:
                stress.slwlrs()
            if lst == 2:
                stress.udpflood()
            else:
                a_main()

        if es == 7:
            print('   \033[1;32mPassWard Tools\033[0;0m')
            ls.psstools()
            lsp = int(input('  >> '))
            if lsp == 1:
                passtool.passgen()
            if lsp == 2:
                hashtool.hashkillr()
            if lsp == 3:
                hashtool.hashkillw()
            else:
                a_main()

        if es == 8:
            print('   \033[1;32mA-xex Console\033[0;0m')
            ls.console()
            lsc = int(input('  >> '))
            if lsc == 1:
                listener.liste()
            if lsc == 2:
                console.payfac()
            if lsc == 3:
                listener.bindtcp()
            if lsc == 4:
                listener.bindudp()
            if lsc == 5:
                console.payfac2()
            else:
                a_main()


    except:
        print('Try a number in list.')
        exit('\033[31m   ----Thanks For Using A-xex----\033[0;0m')








