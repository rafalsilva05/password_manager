# Password manager
# A simple code to strengthen my programming skills
# Focusing in storing and organizing passwords in a not aproprieted manner, storing the informations on a txt file

# First I will ask the user his name and a password

import streamlit as st
import pandas as pd
import application.authentication as aut

# Application tittle
st.set_page_config(page_title="password manager")
st.markdown("<h1 style='text-align: center;'>Password manager</h1>", unsafe_allow_html=True)

# Definition of each pages layout and functionality

#def authentication():
#    pass

        
        
# Management of the application navegation

if 'page' not in st.session_state:
    st.session_state.page = 'authentication'


match st.session_state.page:
    case 'authentication':
        aut.authentication()