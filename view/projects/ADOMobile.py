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
# st.markdown("""
#     <style>
#         /* Hilangkan header Streamlit */
#         header {
#             visibility: hidden;
#         }

#         /* Hilangkan footer Streamlit */
#         footer {
#             visibility: hidden;
#         }

#         /* Hapus padding atas halaman supaya custom header menempel ke atas */
#         .block-container {
#             padding-top: 0rem;
#         }
#     </style>
# """, unsafe_allow_html=True)


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
        <div class="custom-header-title">ADO Mobile</div>
        <div class="custom-header-subtitle">Data pada fitur ini merupakan data IPM Kabupaten Jember</div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Jumlah Pelanggan Aktif")
        graphCB_Populasi()  # altair_chart masuk ke dalam!

with col2:
    with st.container(border=True):
        st.subheader("Distribusi ARPU per Kecamatan")
        graph_Arpu()

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("Jumlah Persebaran Menara BTS")
        graph_Site_pie()

with col4:
    with st.container(border=True):
        st.subheader("Distribusi Outlet Mitra")
        graph_OUTLETPJP_pie()

with st.container(border=True):
    st.title("FB Share Reg & Youth per Kecamatan")
    graph_FBREG_FBYouth()

table()
refreshButton()