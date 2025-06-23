import streamlit as st
from model import *

ADOMobileconn = gsheet_ADOIH_connection()
df = ADOMobileconn.read(ttl=2)

@st.cache_data
def get_Kabupaten_data(): 
    try:
        return df['KABUPATEN'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_ListAktif_data(): 
    try:
        return [f"{x:.3f}" for x in df['LIS AKTIF']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_ListNonAktif_data(): 
    try:
        return [f"{x:.3f}" for x in df['LIS NON AKTIF']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_TotalHousehold_data(): 
    try:
        return [f"{x:.3f}" for x in df['TOTAL HOUSEHOLD']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_PortAvail_data(): 
    try:
        return [f"{x:.3f}" for x in df['PORT AVAILABLE']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_TotalPort_data(): 
    try:
        return [f"{x:.3f}" for x in df['TOTAL PORT']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_PortUnavail_data(): 
    try:
        return [f"{x:.3f}" for x in df['PORT UNAVAILABLE']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_WifiShare_data(): 
    try:
        return df['WIFI SHARE'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_ODP_data(): 
    try:
        return [f"{x:.3f}" for x in df['TOTAL ODP']]
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_CloseComp_data(): 
    try:
        return df['CLOSE COMP'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_PENETRATION_RATE(): 
    try:
        return df['PENETRATION RATE'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_PORT_SHARE(): 
    try:
        return df['PORT SHARE'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None