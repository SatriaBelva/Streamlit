import streamlit as st
from model import *

ADOMobileconn = gsheet_ADOIH_connection()
df = ADOMobileconn.read(ttl=2)

def get_Kabupaten_data(): 
    try:
        return df['KABUPATEN'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_ListAktif_data(): 
    try:
        return [f"{x:.3f}" for x in df['LIS AKTIF']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_TotalHousehold_data(): 
    try:
        return [f"{x:.3f}" for x in df['TOTAL HOUSEHOLD']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_PortAvail_data(): 
    try:
        return [f"{x:.3f}" for x in df['PORT AVAILABLE']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_TotalPort_data(): 
    try:
        return [f"{x:.3f}" for x in df['TOTAL PORT']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_WifiShare_data(): 
    try:
        return df['WIFI SHARE'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_ODP_data(): 
    try:
        return [f"{x:.3f}" for x in df['TOTAL ODP']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_CloseComp_data(): 
    try:
        return df['CLOSE COMP'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None


    
