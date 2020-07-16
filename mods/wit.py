import tkinter
from tkinter import messagebox
import random
import time 


def wit():
    try:
        file = open("log.txt", "r")
        print(' Hi ',file)
        #print('o arquivo existe')
    except:
        s = "1234567890"
        l = 5
        c = "".join(random.sample(s,l))
        #print(c)

        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("Information Key", c)
        print('  Input Key')
        z = input(' >> ')

        kla = c
        if kla == z:
	    print(' [OK]')
	    print(' Set Your H4CK3R Name')
	    nme = input(' >> ')
            print(' [OK]')
            new_file_name = "log.txt"
            new_file = open(new_file_name, 'w')
            new_file.write(nme)
            new_file.close()
            #print('o arquivo nao existe mas esta sendo criado')

        else:
            print('[!]')
	    time.sleep(1)
            wit()

