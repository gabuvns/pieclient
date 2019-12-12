from datetime import datetime
import asyncore, hashlib
from smtpd import SMTPServer
from simplecrypt import encrypt, decrypt

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print("You will need the following password to decrypt the messages!!")
        server_pass = input("Server password, DO NOT LOSE OR ALL EMAIL WILL BE LOST: ")

        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
            self.no)
        print(filename)
        f = open(filename, 'wb')
        
        ciphertext = encrypt(server_pass, data)
       
        f.write(ciphertext)
        f.close
        print('%s saved.' % filename)
        self.no += 1


def run():
    EmlServer(('localhost', 1025), None)
    print("Server up")
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()