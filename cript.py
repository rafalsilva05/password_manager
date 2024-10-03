import pandas as pd
from cryptography.fernet import Fernet


def add_user_password(new_name, new_pswd, master_pwd):
    fer = create_key(master_pwd)
    df = pd.DataFrame({'name': [new_name], 'password': [fer.encrypt(new_pswd.encode())]})
    df.to_csv("tabela.csv", index=False)
    print(df)


def find_user_passwords():
    pass

def verify_key(master_pwd):
    return master_pwd


def create_key(master_pwd):
    key = load_key() + master_pwd.encode()
    return Fernet(key)

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key(): 
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key