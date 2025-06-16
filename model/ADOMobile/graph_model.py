import streamlit as st
from model import *

ADOMobileconn = gsheet_ADOMobile_connection()
df = ADOMobileconn.read(ttl=2)

def get_Kabupaten_data(): 
    try:
        return df['KABUPATEN'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_CB_data(): 
    try:
        return df['CB'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_Populasi_data(): 
    try:
        return df['POPULASI'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_FBShareREG_data(): 
    try:
        return df['FB SHARE REG'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_FBShareYouth_data(): 
    try:
        return df['FB SHARE YOUTH'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_OUTLETPJP_data(): 
    try:
        return df['OUTLET PJP'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_Arpu_data(): 
    try:
        return df['ARPU'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_Site_data(): 
    try:
        return df['SITE'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None


    def get_Total_Daya_Beli_Masyarakat_data(): 
        try:
            return df['Total Daya Beli Masyarakat'].tolist()
        except Exception as e:
            st.error("Gagal mengambil gsheet.")
            st.exception(e)
            return None
