# Password manager
# A simple code to strengthen my programming skills
# Focusing in storing and organizing passwords in a not aproprieted manner, storing the informations on a txt file

# First I will ask the user his name and a password

import streamlit as st

# Application tittle
st.set_page_config(page_title="password manager")


# definition of each layout of the page
# I'd preffer to put in functions for a better look to the code

# Access user passwords function will search for the passwords for the user names and uncriptography using the global key
def access_user_passwords():
    st.title("acessar senha de usuário")

    # This part is for the aplication of the function

    if st.button("adicionar senha"):
        st.session_state.page = 'add_new_password'
        st.rerun()

# Add new password will criptograph the password and associate with the user name, to acess you will need the global key
def add_new_password():
    st.title("adicionar senha a um usuário")

    # This part is for the aplication of the function

    if st.button("acessar usuário"):
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
