import pandas as pd

user_table = pd.read_csv("./tables/users.csv")    

# Excepitions deffinition
class UserNotFound(Exception):
    pass

class UserAlreadyExist(Exception):
    pass

# Functions deffinition
def get_user(username):
    try:
        user_row = find_user(username)
        return user_table.loc[user_row]
    except UserNotFound:
        raise UserNotFound

def add_User(username, password):
    try:
        pass
        if find_user(username):
            pass
    except UserNotFound:
        user_table.loc[len(user_table.index)] = [username, password]
        user_table.to_csv("./tables/users.csv", index=False)
        print("added")
        return
    raise UserAlreadyExist

def find_user(username) -> int:
    for i in user_table.index:
        if user_table.loc[i][0] == username:
            return i
    raise UserNotFound
