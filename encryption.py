from cryptography.fernet import Fernet

def encrypt_file(key, file_path):
    with open(file_path, 'rb+') as file:
        data = file.read()
        encryptedData = key.encrypt(data)
        file.seek(0)
        file.write(encryptedData)
        file.truncate()


def decrypt_file(key, file_path):
    with open(file_path, 'rb+') as file:
        encryptedData = file.read()
        decryptedData = key.decrypt(encryptedData)
        file.seek(0)
        file.write(decryptedData)
        file.truncate()
        
    