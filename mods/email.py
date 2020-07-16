from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from mods import a_main
import email
import imaplib

def sendmailmenssage():
    try:
        msg = MIMEMultipart()

        message = input('message> ')

        msg['From'] = input(' from> ')
        password = input(' password> ')
        msg['To'] = input(' to> ')
        msg['Subject'] = input(' subject> ')

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()
        print ("successfully sent email to %s:" % (msg['To']))
        input('press enter')
        a_main.a_main()

    except:
        print('\n')
        print('  [\033[1;31merror\033[0;0m]-Your email is blocking.')
        print('  [\033[1;31m!\033[0;0m]-you need to allow this functionality.')
        input('press enter')
