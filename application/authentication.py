import streamlit as st
import pandas as pd
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import tables.users as users_table



def authentication():
    # Tittle and subtittle
    st.header("Authentication")
    st.text("To enter the password manager, please, insert your user's informations")

    # Input camps
    username_input_text = st.text_input("Username", placeholder="Enter your username")
    password_input_text = st.text_input("Password", type="password", placeholder="Enter your password")

    # Authentication button
    # Authentication verify's if user exist and give's access to the User passwords.
    if st.button("Authenticate"):
        # Verifys if user filled the inputs
        if not username_input_text and not password_input_text:
            st.error("Please, fill the blanck filds!")
        
        else:
            try:
                tokien = users_table.get_user(username_input_text)[1]
                st.text(tokien)
                st.text(decrypt_msg(password_input_text, tokien))
            except users_table.UserNotFound:
                st.error("User not found!")



    # Add user button
    # Add new User to users_table
    st.text("\ndont have a user?")
    if st.button("Add user"):
        # Verifys if user filled the inputs
        if not username_input_text and not password_input_text:
            st.error("Please, fill the blanck filds!")


        # Verifys if User already exist
        else:
            try:
                password = encryptograph_password(password_input_text)
                users_table.add_User(username_input_text, password)
            except users_table.UserAlreadyExist:    
                st.error("User already exist!")



def generateKey():
    salt = os.urandom(16)
    with open("key.key", "wb") as key_file:
        key_file.write(salt)

def loadKey():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def encryptograph_password(password):
    salt = loadKey()
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
    salt = loadKey()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    return f.decrypt(msg.encode()).decode()
