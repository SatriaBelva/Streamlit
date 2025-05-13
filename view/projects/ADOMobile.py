import streamlit as st
import pandas as pd
from controller import *
from model import *

st.markdown(
    """
    <style>
    section.main > div {background-color: #f0f2f6;}

    div[data-testid="stVerticalBlock"] > div[style*="border"] {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        overflow: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1 :
    with st.container(border=True, height=700):
        st.subheader("Jumlah Pelanggan Aktif")
        graphCB_Populasi()
with col2 :
    with st.container(border=True, height=700):
        st.subheader("Distribusi ARPU per Kecamatan")
        graph_Arpu()

col3, col2 = st.columns(2)
with col3 :
    with st.container(border=True, height=700):
        st.subheader("Jumlah Persebaran Menara BTS")
        graph_Site_pie()
with col2 :
    with st.container(border=True, height=700):
        st.subheader("Distribusi Outlet Mitra")
        graph_OUTLETPJP_pie()

with st.container(border=True, height=700):
    st.title("FB Share Reg & Youth per Kecamatan")
    graph_FBREG_FBYouth()

table()

refreshButton()