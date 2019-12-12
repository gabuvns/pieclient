#Used to decrypt email_server
import glob
from simplecrypt import encrypt, decrypt

glob.glob('*.eml')
for file in glob.glob("*.eml"):
    print("Opening: " + file)
    file = open(file, encoding = "ISO-8859-1")
    words = file.read()
    print(words)
    file_pass = input("File password = ")
    decripttext = decrypt(file_pass, bytes(words,  encoding = "ISO-8859-1"))
    print("Conteudo do arquivo: " + str(decripttext))



