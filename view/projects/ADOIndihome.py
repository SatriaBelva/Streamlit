import streamlit as st
import pandas as pd
from controller import *
from model import *

col1, col2 = st.columns(2)
with col1 :
    st.subheader("Pengguna Aktif IndiHome")
    graph_ListAktif_TotalHousehold()
with col2 :
    st.subheader("Port")
    graph_PortAvail_TotalPort()

col1, col2 = st.columns(2)
with col1 :
    st.subheader("Pangsa Pasar Layanan Internet")
    graph_WifiShare()
with col2 :
    st.subheader("Jumlah Optical Distribution Point")
    graph_ODP()

tableADOIH()