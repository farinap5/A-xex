import hashlib
#from mods import a_main
import time
import random
#from mods import a_main

def hashkillr():
    s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passlen = 5

    #key = "21232f297a57a5a743894a0e4a801fc3" - admin
    print("   Hash MD5 BruteForce Random Value")
    print("   Set Hash ")
    key = input("  > ")
    passlen = int(input("  password length: "))
    print("   [\033[1;32mOK\033[0;0m] - ", key)


    while True:
        try:

            password = "".join(random.sample(s, passlen))

            h = hashlib.md5()
            h.update(password.encode("utf-8"))
            cat = h.hexdigest()
            if cat == key:
                print("   ",cat," = ",key," > ", password)
                break
                input("press enter")
                a_main.a_main()
            else:
                print("   ",cat," > ",key," > ",password, end="\r")
        except:
            break

def hashkillw():


    #key = "21232f297a57a5a743894a0e4a801fc3"
    print("   Hash MD5 BruteForce")
    print("   Set Hash ")
    key = input("  > ")
    arq = input("  set WordList: ")
    print("   [\033[1;32mOK\033[0;0m] - ", key)

    mywl = []

    file = open(arq).read().splitlines()
    for line in file:
        mywl.append(line)

    for l in mywl:
        try:
            h = hashlib.md5(l)
            cat = h.hexdigest()
            if cat == key:
                print("   ",cat," = ",key," > ", l)
                break
                input("press enter")
                a_main.a_main()
            else:
                print("   ",cat," > ",key," > ",l, end="\r")
        except:
            break
