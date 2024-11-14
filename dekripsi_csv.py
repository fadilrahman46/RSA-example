# import required module
from cryptography.fernet import Fernet

# key generation
with open('filekey.key', 'wb') as filekey:
    filekey.readlines()
# using the key
fernet = Fernet(filekey)
 
# opening the encrypted file
with open('file_tes_encrypted.csv', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('file_tes_decrypted.csv', 'wb') as dec_file:
    dec_file.write(decrypted)