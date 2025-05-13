import streamlit as st
import pandas as pd
from controller import *
from model import *

col1, col2 = st.columns(2)
with col1 :
    st.subheader("Jumlah Pelanggan Aktif")
    graphCB_Populasi()
with col2 :
    st.subheader("FB Share Reg & Youth per Kecamatan")
    graph_FBREG_FBYouth()

col3, col2 = st.columns(2)
with col3 :
    st.subheader("umlah Persebaran Menara BTS")
    graph_Site_pie()
with col2 :
    st.subheader("Distribusi Outlet Mitra")
    graph_OUTLETPJP_pie()

st.title("JDistribusi ARPU per Kecamatan")
graph_Arpu()

table()

refreshButton()