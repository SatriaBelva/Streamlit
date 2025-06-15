import streamlit as st
import pandas as pd
from controller import *
from model import *
from PIL import Image
import base64
from io import BytesIO

def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

# Masukkan path gambar lokal Anda
image_path = r"assets/foto_telkom_katanya.png"
img_base64 = image_to_base64(image_path)

# Styling header dan layout
st.markdown("""
    <style>
        .main > div:first-child {
            padding-top: 0rem;
        }

        .custom-header-container {
            background: linear-gradient(to right, #FD9B2A, #E30511);
            border-radius: 0 0 0px 80px;
            height: 135px;
            display: flex;
            align-items: center;
            color: white;
            margin-top: -3.5rem;
            margin-bottom: 2rem;
            padding-left: 50px;
            padding-right: 158px;
        }

        .custom-header-container img {
            height: 128px;

        }

        .header-text-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            flex: 1;
        }

        .custom-header-title {
            font-size: 36px;
            font-weight: bold;
            margin: 0;
        }

        .custom-header-subtitle {
            font-size: 16px;
            text-align: center;
            width: 80%;
            font-weight: normal;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Tampilkan header
st.markdown(f"""
    <div class="custom-header-container">
        <img src="data:image/png;base64,{img_base64}" alt="Header Image"/>
        <div class="header-text-container">
            <div class="custom-header-title">ADO IndiHome</div>
            <div class="custom-header-subtitle">Analisis infrastruktur IndiHome untuk perluasan jaringan yang tepat sasaran<br>Jember</div>
        </div>
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
        graph_WifiShare()
with col2 :
    with st.container(border=True):
        st.subheader("Jumlah Titik ODP")
        # graph_ODP()
        graph_ODP()

tableADOIH()

display_strategy_ui()