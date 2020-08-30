import os
import time

def checkdep():
    os.system("clear")
    def masc():
        print("""\033[1;32m
                                  
        A-xex        ██████████████████                                                
      Framework    ██████          ██████
                  ██                    ██      
                 ██    ████      ████    ██
                 ██  ██   ██    ██   ██  ██
                ██                        ██
                ██                        ██   
                ██  ██                ██  ██
                ██    ██    ████    ██    ██
               █████    ████    ████    █████
               █████                    █████
              ████████       ██       ████████
            ████████████     ██     ████████████
            ██████████████        ██████████████   
            ████████████████████████████████████                                                         
                     Checking Libraries
                This May Take A Few Minutes
        
    \033[0;0m """)


    def count():
        lis = ["|>-----------|  0%|","|=>----------| 10%|","|==>---------| 20%|","|===>--------| 30%|","|====>-------| 40%|","|=====>------| 50%|","|======>-----| 60%|","|=======>----| 70%|","|========>---| 80%|","|=========>--| 90%|","|==========>-|100%|"]
        for i in lis:
            print("               ",i, end="\r")
            time.sleep(0.05)



    def trings():
        try:
            import os
        except:
            print("error")
            os.system("sudo python3 -m pip install os")
        count()
        try:
            from urllib import request
        except:
            print("error")
            os.system("sudo python3 -m pip install urllib")
        count()
        try:
            import subprocess
        except:
            print("error")
            os.system("sudo python3 -m pip install subprocess")
        count()
        try:
            import requests
        except:
            print("error")
            os.system("sudo python3 -m pip install requests")
        count()
        try:
            import socket
        except:
            print("error")
            os.system("sudo python3 -m pip install socket")
        count()
        try:
            import whois
        except:
            print("error")
            os.system("sudo python3 -m pip install whois")
        count()
        try:
            from ipwhois import IPWhois
        except:
            print("error")
            os.system("sudo python3 -m pip install IPWhois")
        count()
        try:
            import ipwhois
        except:
            print("error")
            os.system("sudo python3 -m pip install ipwhois")
        count()
        try:
            import smtplib
        except:
            print("error")
            os.system("sudo python3 -m pip install smtplib")
        count()
        try:
            import email
        except:
            print("error")
            os.system("sudo python3 -m pip install email")
        count()
        try:
            import imaplib
        except:
            print("error")
            os.system("sudo python3 -m pip install imaplib")
        count()
        try:
            from email.mime.multipart import MIMEMultipart
        except:
            print("error")
            os.system("sudo python3 -m pip install email.mime.multipart")
        count()
        try:
            from email.mime.text import MIMEText
        except:
            print("error")
            os.system("sudo python3 -m pip install email.mime.text")
        count()
        try:
            import hashlib
        except:
            print("error")
            os.system("sudo python3 -m pip install hashlib")
        count()
        try:
            import time
        except:
            print("error")
            os.system("sudo python3 -m pip install time")
        count()
        try:
            import random
        except:
            print("error")
            os.system("sudo python3 -m pip install random")
        count()
        try:
            import platform
        except:
            print("error")
            os.system("sudo python3 -m pip install platform")
        count()
        try:
            import threading
        except:
            print("error")
            os.system("sudo python3 -m pip install threading")
        count()
        try:
            import sys
        except:
            print("error")
            os.system("sudo python3 -m pip install sys")
        count()
        try:
            import dns.renderer
        except:
            print("error")
            os.system("sudo python3 -m pip install dns")
        count()
        try:
            import re
        except:
            print("error")
            os.system("sudo python3 -m pip install re")
        count()
        try:
            import matplotlib.pyplot as plt
        except:
            print("error")
            os.system("sudo python3 -m pip install matplotlib")
        count()

    masc()
    trings()
    os.system("clear")
    print("""\033[1;32m
    
        ╔══════════════════════════╗
        Your System Is Ready To Work
        ╚══════════════════════════╝
    
    \033[0;0m""")
    input("press enter")
    os.system("clear")


try:
    checkdep()
except:
    exit("Quiting!")


