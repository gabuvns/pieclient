#PieCLIent
#Email client with python3

from os import system, name
import ssl, smtplib, inspect


def detect_input(user_input):
    if user_input in "help":
        print_help()
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
            print("You must first login to use this command")
    
    else:
        print("Invalid Command")

def get_user_credentials():
    user_provider = input("Type your provider: ")
    user_email = input("Type your email: ")
    user_password = input("Type your password: ")
    return user_provider, user_email, user_password

def print_help():
    print("connect - get user information")
    print("clear - clears the screen" )
    print("exit - quits de program")
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


def connect(user_provider, user_email, user_password):

    if user_provider in "gmail":
        print("Gmail Selected")
        # Para ssl
        port = 465
        #starting a secure connection
        context = ssl.create_default_context()
  
    else:
        print("Using gmail as default")
        port = 465
        context = ssl.create_default_context()


    print("Opening connection")

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(user_email, user_password)

        print("Connection established")
        print("You can now use the extra commands")
        while 1:
            user_input = input("Insert your command: ")
            can_command = detect_input(user_input)
            # Send email
            if can_command == 1:
                receiver_email, message = send()
                server.sendmail(user_email, receiver_email, message)
                print("Email Sent")


print("Welcome to PieCLIent!\nType help for a list of commands")
print("Type connect to log-in")

while 1:
    user_input = input("Insert your command: ")
    detect_input(user_input)


