# Password manager
# A simple code to strengthen my programming skills
# Focusing in storing and organizing passwords in a not aproprieted manner, storing the informations on a txt file

# First I will ask the user his name and a password

import streamlit as st
import pandas as pd

# Application tittle
st.title("Password_manager")

# Deffining object User
class User:
    def __init__(self, name, pswd) -> None:
        self.name = name
        self.pswd = pswd

    def __str__(self) -> str:
        return f"{self.name}"
    
    def __dict__(self):
        return {'name': self.name, 'password': list(self.pswd)}
    

    
def add_user(username, password):
    # new_user = User(username, password)

    df = pd.DataFrame({'name': [username], 'password': [password]})
    print(df)
    df.to_csv("tabela.csv", index=False)
    
    

# User inputs
username = st.text_input("Enter your Username:")
password = st.text_input("Enter your password:", type="password")

if st.button("Create User:"):
    if username and password:
        add_user(username, password)
        st.success(f"User {username} created")
    else:
        st.error("Please try again")
