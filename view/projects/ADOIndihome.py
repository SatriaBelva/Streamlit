import streamlit as st
import pandas as pd
from controller import *
from model import *

col1, col2 = st.columns(2)
with col1 :
    st.subheader("Pengguna Aktif IndiHome")
    graph_ListAktif_TotalHousehold()
with col2 :
    st.subheader("Ketersediaan Port IndiHome")
    graph_PortAvail_TotalPort()

col1, col2 = st.columns(2)
with col1 :
    st.subheader("Jumlah Persebaran WIFI")
    # graph_WifiShare()
    graph_WifiShare_pie()
with col2 :
    st.subheader("Jumlah Titik ODP")
    # graph_ODP()
    graph_ODP_pie()

tableADOIH()