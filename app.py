# Password manager
# A simple code to strengthen my programming skills
# Focusing in storing and organizing passwords in a not aproprieted manner, storing the informations on a txt file

# First I will ask the user his name and a password

import streamlit as st
import pandas as pd
import application.authentication as aut
import application.pwd_manager as pwd
from application.token import Token

# Application tittle
st.set_page_config(page_title="password manager")
st.markdown("<h1 style='text-align: center;'>Password manager</h1>", unsafe_allow_html=True) 

# Management of the application navegation

if 'page' not in st.session_state:
    st.session_state.page = 'authentication'
if 'token' not in st.session_state:
    st.session_state.token = None

match st.session_state.page:
    case 'authentication':
        st.session_state.token = aut.authentication()
        if st.session_state.token:
            print("end authentication")
            pwd.pwd_manager(st.session_state.token)
            st.session_state.page = 'password_manager'
            st.rerun()
    case 'password_manager':
        print("passw man")
        if st.session_state.token:
            print("aaaa")
            pwd.pwd_manager(st.session_state.token)
        else:
            print("oxi")
            st.session_state.page = 'authentication'

