import smtpd
import asyncore

class CustomSMTPServe(smtpd.SMTPServer):
   def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to:', rcpttos)
        print('Message length:', len(data))
    

def run():
    foo = CustomSMTPServe(('localhost', 1025), None)
    print("Flag")
    asyncore.loop()

run()