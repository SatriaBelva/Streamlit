import streamlit as st
from model import *

MarketCompetitionconn = gsheet_MarketCompetition_connection()
df = MarketCompetitionconn.read(ttl=2)

def get_Kabupaten_data(): 
    try:
        return df['KABUPATEN'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_FacebookShare_data(): 
    try:
        return df['FB SHARE REG'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_StatugReg_data(): 
    try:
        return df['STATUS REG'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_CloseCompetitionReg_data(): 
    try:
        return df['CLOSE COMP REG'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_FacebookShareYouth_data(): 
    try:
        return df['FB SHARE YOUTH'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_StatusYouth_data(): 
    try:
        return df['STATUS YOUTH'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_CloseCompetitionYouth_data(): 
    try:
        return df['CLOSE COMP YOUTH'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None