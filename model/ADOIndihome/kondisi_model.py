import streamlit as st
from model import *

Summaryconn = gsheet_Summary_connection()
df = Summaryconn.read(ttl=2)

def get_kondisi(): 
    try:
        return df['Kondisi'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_Emoji(): 
    try:
        return df['Emoji'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_Judul(): 
    try:
        return df['Judul'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_Interpretasi(): 
    try:
        return df['Interpretasi'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_Strategi(): 
    try:
        return df['Strategi'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None