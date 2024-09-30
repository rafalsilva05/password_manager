# Password manager
# A simple code to strengthen my programming skills
# Focusing in storing and organizing passwords in a not aproprieted manner, storing the informations on a txt file

# First I will ask the user his name and a password

import streamlit as st

# Application tittle
st.title("Password_manager")

# Deffining object User
class User:
    def __init__(self, name, pswd) -> None:
        self.name = name
        self.pswd = pswd

    def __str__(self) -> str:
        return f"{self.name}"
