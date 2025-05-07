import streamlit as st
from model.db_connection import get_connection

conn = get_connection()
    
def get_email_data() :
    try:
        return conn.query('SELECT email FROM email;', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data kontak.")
        st.exception(e)
        return None
    
def get_account_data() : 
    try:
        return conn.query('SELECT * FROM `user`', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data kontak.")
        st.exception(e)
        return None
    