import streamlit as st
import pandas as pd
from controller import *
from model import *

# col1, col2 = st.columns(2)

# with col1 :
#     with st.container(border=True, height=700):
#         st.subheader("Jumlah Pelanggan Aktif")
#         graphCB_Populasi()
# with col2 :
#     with st.container(border=True, height=700):
#         st.subheader("Distribusi ARPU per Kecamatan")
#         graph_Arpu()

# col3, col2 = st.columns(2)
# with col3 :
#     with st.container(border=True, height=700):
#         st.subheader("Jumlah Persebaran Menara BTS")
#         graph_Site_pie()
# with col2 :
#     with st.container(border=True, height=700):
#         st.subheader("Distribusi Outlet Mitra")
#         graph_OUTLETPJP_pie()

# with st.container(border=True, height=700):
#     st.title("FB Share Reg & Youth per Kecamatan")
#     graph_FBREG_FBYouth()

# table()

def white_container(content_func, height=700):
    """Wrapper untuk konten dalam container putih + border"""
    st.markdown(
        f"""
        <div style="background-color:white; padding:20px; border-radius:10px; 
                    border:1px solid #ddd; height:{height}px; overflow:auto;">
        """,
        unsafe_allow_html=True
    )
    content_func()
    st.markdown("</div>", unsafe_allow_html=True)

# --- Layout 1 ---
col1, col2 = st.columns(2)

with col1:
    white_container(lambda: (
        st.subheader("Jumlah Pelanggan Aktif"),
        graphCB_Populasi()
    ))

with col2:
    white_container(lambda: (
        st.subheader("Distribusi ARPU per Kecamatan"),
        graph_Arpu()
    ))

# --- Layout 2 ---
col3, col4 = st.columns(2)

with col3:
    white_container(lambda: (
        st.subheader("Jumlah Persebaran Menara BTS"),
        graph_Site_pie()
    ))

with col4:
    white_container(lambda: (
        st.subheader("Distribusi Outlet Mitra"),
        graph_OUTLETPJP_pie()
    ))

# --- Full width container ---
white_container(lambda: (
    st.title("FB Share Reg & Youth per Kecamatan"),
    graph_FBREG_FBYouth()
))

# --- Footer components ---
table()

refreshButton()