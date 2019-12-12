#PieCLIent
#Email client with python3

from os import system, name
import ssl, smtplib, inspect, imaplib, getpass, email

def detect_input(user_input):
    if user_input in "help":
        print_help()
    
    elif user_input in "localserver_test":
        test()
    elif  user_input in "clear":
        clear_screen()

    elif user_input in "quit":
        print("Have a good day")
        exit()
  
    elif user_input in "connect":
        if inspect.stack()[1][3] == "connect":
            print("You are alredy connected")
        else:   
            # user_provider, user_email, user_password = get_user_credentials()
            user_email = "tempacc767@gmail.com"
            user_password = "Senhamuitoseguratp2@"
            user_provider = "gmail"
            connect(user_provider, user_email, user_password)

    elif user_input in "send":
        if inspect.stack()[1][3] == "connect":
            return 1;
        else:
            print("You must first connect to use this command")
    elif user_input in "list":
        if inspect.stack()[1][3] == "connect":
            return 2;
        else:
            print("You must first connect to use this command")
    
    else:
        print("Invalid Command")

def test():
    clear_screen()
    print("TEST MODE INITIATED")
    print("Using: testpython@test.com as sender")
    print("Using bla@test.com as receiver")
    
    subject = input("E-mail subject: ")
    user_message = input("Type your message: ")

    with smtplib.SMTP("localhost", 1025) as server:
        FROM = "testpython@test.com"
        TO = "bla@test.com"
        MSG = """Subject: """ + subject  + "\n"+  user_message + "\nSent with PieCLIent"
        server.sendmail(FROM, TO, MSG)
        print("email sent")
        # user_email = 'tempacc767@gmail.com'
        # user_password = 'Senhamuitoseguratp2@'
        # server.login(user_email, user_password)

def get_user_credentials():
    user_provider = input("Type your provider: ")
    user_email = input("Type your email: ")
    user_password = input("Type your password: ")
    return user_provider, user_email, user_password

def print_help():
    print("connect - get user information")
    print("set - define if it will use POP3 or IMAP, impap is used by default")
    print("clear - clears the screen" )
    print("exit - quits de program")
    print("localserver_test - enters test mode with, must connect to 'localhost' on port 1025")
    print("You must first connect for the following commands:")
    print("send - sends an email")
    print("list - lists your emails")

def clear_screen():
   if name == 'nt':
      _ = system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')

def send():
    receiver_email = input("Receiver email: ")
    subject = input("E-mail subject: ")
    user_message = input("Type your message: ")

    # message = "From:" + user_email + "\n"
    # message += "To: " + receiver_email + "\n"
    message = """Subject: """ + subject  + "\n"+  user_message + "\nSent with PieCLIent"

    return receiver_email, message


def list(user_email, user_password, port_imap):
    print("Opening IMAP connection")
    
    imap_connect = imaplib.IMAP4_SSL("imap.gmail.com", port_imap)
    imap_connect.login(user_email, user_password)

    print("IMAP connection established")

    imap_connect.select('inbox')

    type, data = imap_connect.search(None, 'ALL')
    mail_ids = data[0]
    if len(mail_ids) == 0:
        print("You have no unread mails")
    else:
        print("You have " + str(len(mail_ids)) + "  emails")
        # id_list = mail_ids.split()   
        # first_email_id = int(id_list[0])
        # latest_email_id = int(id_list[-1])
        # for i in range(first_email_id, latest_email_id):
        #     typ, data = imap_connect.fetch(str(i), '(RFC822)' )
        #     for response_part in data:
        #         if isinstance(response_part, tuple):
        #             msg = email.message_from_string(str(response_part[1]))
        #             email_subject =str(msg['subject']) 
        #             email_from = str(msg['from'])
        #             print ('From : ' + email_from + '\n')
        #             print ('Subject : ' + email_subject + '\n')




def connect(user_provider, user_email, user_password):

    if user_provider in "gmail":
        print("Gmail Selected")
        # Para ssl
        port_smtp = 465
        port_imap = 993
        #starting a secure connection
        context = ssl.create_default_context()
  
    else:
        print("Using gmail as default")
        port_smtp = 465
        port_imap = 993

        context = ssl.create_default_context()

    while 1:

        user_input = input("Insert your command: ")
        can_command = detect_input(user_input)

        # Send email
        if can_command == 1:
            print("Opening SMTP connection")
            with smtplib.SMTP_SSL("smtp.gmail.com", port_smtp, context=context) as server:
                server.login(user_email, user_password)

                print("SMTP connection established")
            
                print("You can now send e-mails")
                receiver_email, message = send()
                server.sendmail(user_email, receiver_email, message)
                print("Email Sent")
                print("Disconnecting SMTP")
                server.quit()
        
        # List Emails
        if can_command == 2:
            list(user_email, user_password, port_imap)
        

print("Welcome to PieCLIent!\nType help for a list of commands")
print("Type connect to log-in")

while 1:
    user_input = input("Insert your command: ")
    can_command = detect_input(user_input)


