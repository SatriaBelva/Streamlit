import streamlit as st
from model import *

ADOMobileconn = gsheet_ADOMobile_connection()
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
def get_Populasi_data(): 
    try:
        return df['POPULASI'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_ARPU_data(): 
    try:
        return df['ARPU'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_CB_data(): 
    try:
        return df['CB'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_PenetrasiCB_data(): 
    try:
        return df['PENETRASI CB'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_OutletPJP_data(): 
    try:
        return df['OUTLET PJP'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_Site_data(): 
    try:
        return df['SITE'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_CoverageShare_data(): 
    try:
        return df['COVERAGE SHARE'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_FacebookShare_data(): 
    try:
        return df['FB SHARE REG'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_StatugReg_data(): 
    try:
        return df['STATUS REG'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_CloseCompetitionReg_data(): 
    try:
        return df['CLOSE COMP REG'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_FacebookShareYouth_data(): 
    try:
        return df['FB SHARE YOUTH'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_StatusYouth_data(): 
    try:
        return df['STATUS YOUTH'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data    
def get_CloseCompetitionYouth_data(): 
    try:
        return df['CLOSE COMP YOUTH'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_PelajarMahasiswa_data(): 
    try:
        return df['Pelajar Mahasiswa'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_IRT_data(): 
    try:
        return df['IRT'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_Nelayan_Perdagangan_Wiraswasta_data(): 
    try:
        return df['Nelayan, Perdagangan, Wiraswasta'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_Total_Usia_Produktif_data(): 
    try:
        return df['Total Usia Produktif'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None

@st.cache_data
def get_Total_Daya_Beli_Masyarakat_data(): 
    try:
        return df['Total Daya Beli Masyarakat'].tolist()
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
