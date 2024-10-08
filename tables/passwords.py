import pandas as pd


pwd_table = pd.read_csv("./tables/passwords.csv")    

# Excepitions deffinition
class UserNotFound(Exception):
    pass

class UserAlreadyExist(Exception):
    pass

# Functions deffinition
def get_user_passwords(username):
    try:
        ret_table = pd.DataFrame({'name':[],'password':[]})
        for i in pwd_table.index:
            if pwd_table.loc[i][0] == username:
                ret_table.loc[len(ret_table.index)] = pwd_table.loc[i]
        return ret_table
    except UserNotFound:
        raise UserNotFound

def add_password(username, password):
    pwd_table.loc[len(pwd_table.index)] = [username, password]
    pwd_table.to_csv("./tables/passwords.csv", index=False)

def remove_password(username, password):
    new_table = pwd_table.drop(columns=[find_password(username,password)])
    new_table.to_csv("./tables/passwords.csv")

def find_password(username, password):
        for i in pwd_table.index:
            if pwd_table.loc[i][0] == username and pwd_table.loc[i][1] == password:
                print(i)
                return i
