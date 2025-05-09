import streamlit as st
import pandas as pd
from controller import *
from model import *

col1, col2 = st.columns(2)
with col1 :
    st.title("Jumlah Pelanggan Aktif")
    graphCB_Populasi()
with col2 :
    st.title("FB Share Reg & Youth per Kecamatan")
    graph_FBREG_FBYouth()

col3, col2 = st.columns(2)
with col3 :
    st.title("Distribusi ARPU per Kecamatan")
    # graph_ARPU()
    graph_Arpu()
with col2 :
    st.title("Distribusi Outlet Mitra")
    graph_OUTLETPJP()

st.title("Jumlah Persebaran Menara BTS")
graph_Site()

table()

refreshButton()