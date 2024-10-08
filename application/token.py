import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Token:
    _SALT_KEY_PATH = "key.key"

    def __init__(self, username, password) -> None:
        self.username = username
        salt = self.loadSalt()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def enc_token(self, msg):
        return Fernet(self.key).encrypt(msg.encode()).decode()
    
    def dec_token(self, token):
        return Fernet(self.key).decrypt(token).decode()
        
    def loadSalt(self):
        with open(self._SALT_KEY_PATH, "rb") as key_file:
            key = key_file.read()
        return key
        

def createSalt():
    salt = os.urandom(16)
    with open("key.key", "wb") as key_file:
        key_file.write(salt)

def loadSalt():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

'''def genKey(password):
    salt = loadKey()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))'''


def encryptograph_password(password):
    salt = loadSalt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_msg(password, msg):
    salt = loadSalt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    return f.decrypt(msg.encode()).decode()

