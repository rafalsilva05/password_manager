import streamlit as st
import pandas as pd
import tables.passwords as pwd_table
from application.token import Token

def pwd_manager(token=Token):
    # Tittle and subtittle
    st.text("You can remove or add passwords in the camps down the table")
    df_pwd = pwd_table.get_user_passwords(token.username)
    for i in df_pwd.index:
        df_pwd.loc[i][1] = token.dec_token(df_pwd.loc[i][1])
    print(df_pwd)
    st.table(df_pwd)

    password_input_text = st.text_input("Password", placeholder="Enter password")

    if st.button("Add password"):
        if not password_input_text:
            st.error("Please write the password you wanna add")
        else:
            pwd_table.add_password(token.username, token.enc_token(password_input_text))
            st.rerun()
        
    
    if st.button("Remove password"):
        if not password_input_text:
            st.error("Please write the password you wanna add")
        else:
            pwd_table.remove_password(df_pwd.loc[(df_pwd.password == password_input_text)].index)
            st.rerun()
