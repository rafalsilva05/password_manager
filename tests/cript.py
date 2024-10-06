import pandas as pd
import os
from cryptography.fernet import Fernet


def add_user_password(new_name, new_pswd, master_pwd):
    fer = create_key(master_pwd)
    
    if os.path.isfile('..\\tabela.csv'):
        table = pd.read_csv("..\\tabela.csv")
        table.loc[len(table.index)] = [new_name, fer.encrypt(new_pswd.encode()).decode()]
        table.to_csv("..\\tabela.csv", index=False)
    else:
        table = pd.DataFrame({'name': [new_name], 'password': [fer.encrypt(new_pswd.encode()).decode()]})
        table.to_csv("..\\tabela.csv", index=False)



def find_user_passwords(username, m_pwd):
    key = create_key(m_pwd)

    if os.path.isfile('..\\tabela.csv'):
        table = pd.read_csv("..\\tabela.csv")
        ret_table = pd.DataFrame({'name':[], 'password':[]})
        for i in table.index:
            if table.loc[i][0] == username:
                ret_table = ret_table._append({'name':username, 'password':key.decrypt(table.loc[i][1]).decode()}, ignore_index=True    )
        return ret_table
    else:
        return None

def verify_key(master_pwd):
    return master_pwd


def create_key(master_pwd):
        key = load_key() + master_pwd.encode()
        return Fernet(key)

def generate_key():
    key = Fernet.generate_key()
    with open("..\\key.key", "wb") as key_file:
        key_file.write(key)

def load_key(): 
    with open("..\\key.key", "rb") as key_file:
        key = key_file.read()
    return key