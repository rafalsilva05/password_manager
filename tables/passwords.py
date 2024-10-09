import pandas as pd

__PWD_TABLE_PATH__ = "./tables/passwords.csv"

pwd_table = pd.read_csv(__PWD_TABLE_PATH__) 
def load_table():
    global pwd_table
    pwd_table = pd.read_csv(__PWD_TABLE_PATH__)    

# Functions deffinition
def get_user_passwords(username):
    print("======> RET TABLE FROM GET USER PASSWORDS")
    ret_table = pd.DataFrame({'name':[],'password':[]})
    print(pwd_table)
    print("loop:")
    for i in pwd_table.index:
        print(f"index: {i}, row: {pwd_table.loc[i]}")
        if pwd_table.loc[i][1] == username:
            ret_table.loc[i] = pwd_table.loc[i]
    print(ret_table)
    return ret_table

def add_password(username, password):
    pwd_table.loc[len(pwd_table.index)] = [username, password]
    pwd_table.to_csv(__PWD_TABLE_PATH__)

def remove_password(index):
    print("-------> REMOVE PASSWORD")
    print("INDEX: ", index)
    print(pwd_table)
    new_table = pwd_table.drop(index)
    print(new_table)
    print(new_table.reset_index())
    new_table.to_csv(__PWD_TABLE_PATH__)

load_table()