import streamlit as st
from model.db_connection import gsheet_kondisi_connection

kondisiconn = gsheet_kondisi_connection()
df = kondisiconn.read(ttl=2)

@st.cache_data
def get_Kondisi_data(): 
    try:
        return df['Kondisi'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_Judul_data(): 
    try:
        return df['Judul'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
   
@st.cache_data    
def get_Emoji_data(): 
    try:
        return df['Emoji'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_Interpretasi_data(): 
    try:
        return df['Interpretasi'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
@st.cache_data
def get_Strategi_data(): 
    try:
        return df['Strategi'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None