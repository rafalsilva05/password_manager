# Password manager
# A simple code to strengthen my programming skills
# Focusing in storing and organizing passwords in a not aproprieted manner, storing the informations on a txt file

# First I will ask the user his name and a password

import streamlit as st
import tests.cript as cript
import pandas as pd

print("\n\nfor log reasons\n\n===============================NEW RUN===============================")


# Application tittle
st.set_page_config(page_title="password manager")

# definition of each layout of the page
# I'd preffer to put in functions for a better look to the code

# Ask for the User key and verify if the key is valid
def ask_for_m_password():
    with st.popover("Insert key"):
        key = st.text_input("please, write your master password")
        if st.button("Insert Master password"):
            if cript.verify_key():
                return key
            else:
                return None

# Access user passwords function will search for the passwords for the user names and uncriptography using the global key
def access_user_passwords():
    st.title("Get username passwords")

    username = st.text_input("Username")
    master_pwd = st.text_input("Please, write your master password:", type="password")
    
    if st.button("Find passwords"):
        pwd_table = cript.find_user_passwords(username, master_pwd)
        print(pwd_table)
        if not pwd_table.empty:
            st.table(pwd_table)
        else:
            st.error("erro krl")
            st.table(pwd_table)

    if st.button("Go to \'add password\'"):
        st.session_state.page = 'add_new_password'
        st.rerun()

# Add new password will criptograph the password and associate with the user name, to acess you will need the global key
def add_new_password():
    st.title("Add a password to Username")

    username = st.text_input("Username: ")
    new_password = st.text_input("New password:", type="password")
    master_pwd = st.text_input("Please, write your master password:", type="password")

    # try's to add new password to csv
    # If the m_pwd is valid, add's new password to csv file.
    if st.button("Add password"):
        if username and new_password and master_pwd: 
            cript.add_user_password(username, new_password, master_pwd)
            st.session_state.page = 'access_user_password'
            st.rerun()

        # Text input have no anwser -- print error
        else: 
            if not username:
                st.error("Please write the username!")
            if not new_password:
                st.error("Please write the new password!")
            if not master_pwd:
                st.error("Please write the new master password!")

    if st.button("Go to \'get passwords\'"):
        st.session_state.page = 'access_user_password'
        st.rerun()

# Management of the application functionalities

if 'page' not in st.session_state:
    st.session_state.page = 'access_user_password'


match st.session_state.page:
    case 'access_user_password':
        access_user_passwords()
    case 'add_new_password':
        add_new_password()
