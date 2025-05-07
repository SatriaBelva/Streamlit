import streamlit as st
from model.db_connection import get_connection

conn = get_connection()

# def get_kontak_data(): 
#     try:
#         return conn.query('SELECT * FROM kontak LIMIT 2;', ttl=600)
#     except Exception as e:
#         st.error("Gagal mengambil data kontak.")
#         st.exception(e)
#         return None

# def get_Owner_data():
#     try:
#         return conn.query('SELECT Owner FROM kontak;', ttl=600)
#     except Exception as e:
#         st.error("Gagal mengambil data kontak.")
#         st.exception(e)
#         return None 