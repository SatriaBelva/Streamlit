import streamlit as st
import pandas as pd
from controller import *
from model import *

st.markdown("""
    <style>
        /* Hilangkan margin dan padding default body Streamlit */
        .main > div:first-child {
            padding-top: 0rem;
        }

        /* Header container */
        .custom-header-container {
            background-color: #D70000;
            border-radius: 0 0 0px 80px;
            height: 135px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            margin-top: -3.5rem;
            margin-bottom: 2rem;
        }

        .custom-header-title {
            font-size: 36px;
            font-weight: bold;
            margin: 0;
        }

        .custom-header-subtitle {
            font-size: 16px;
            font-weight: normal;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Tampilkan header
st.markdown("""
    <div class="custom-header-container">
        <div class="custom-header-title">ADO IndiHome</div>
        <div class="custom-header-subtitle">Data pada fitur ini merupakan data IPM Kabupaten Jember</div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1 :
    with st.container(border=True):
        st.subheader("Pengguna Aktif IndiHome")
        graph_ListAktif_TotalHousehold()
with col2 :
    with st.container(border=True):
        st.subheader("Ketersediaan Port IndiHome")
        graph_PortAvail_TotalPort()

col1, col2 = st.columns(2)
with col1 :
    with st.container(border=True):
        st.subheader("Jumlah Persebaran WIFI")
        # graph_WifiShare()
        graph_WifiShare_pie()
with col2 :
    with st.container(border=True):
        st.subheader("Jumlah Titik ODP")
        # graph_ODP()
        graph_ODP_pie()

tableADOIH()