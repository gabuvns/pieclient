#!/usr/bin/python
import smtplib

def send():
    print("======================================================================")
    receiver_email = input("Receiver email: ")
    subject = input("E-mail subject: ")
    user_message = input("Type your message: ")

    # message = "From:" + user_email + "\n"
    # message += "To: " + receiver_email + "\n"
    message = """Subject: """ + subject  + "\n"+  user_message + "\nSent with PieCLIent"
    print("======================================================================")

    return receiver_email, message


def connect():

    print("Openning conenction")

    with smtplib.SMTP("localhost", 1025) as server:
        FROM = "testpython@test.com"
        TO = "bla@test.com"
        MSG = "Subject: Test email python\n\nBody of your message!"
        server.sendmail(FROM, TO, MSG)

        # user_email = 'tempacc767@gmail.com'
        # user_password = 'Senhamuitoseguratp2@'
        # server.login(user_email, user_password)

    print("Connected")


def begin():

    connect()

    # user_email, message = send()
    # server.sendmail(user_email, receiver_email, message)



begin()