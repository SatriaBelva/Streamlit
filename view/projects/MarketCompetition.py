import streamlit as st
import pandas as pd
from controller import *
from model import *
from PIL import Image
import base64
from io import BytesIO

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
            <div class="custom-header-title">Market Competition</div>
            <div class="custom-header-subtitle">Informasi status dominasi layanan seluler di wilayah Tapal Kuda, dengan kategori Win untuk area yang didominasi Telkomsel dan Lose untuk area yang didominasi kompetitor terdekatnya, berdasarkan data dari Meta Facebook.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

if 'kecamatan' not in st.session_state:
    st.session_state['kecamatan'] = "Semua"
if 'desa' not in st.session_state:
    st.session_state['desa'] = "Semua"

# map(st.session_state['kecamatan'], st.session_state['desa'])
st.title("Regional Competition")
map_REG_status()
st.title("Youth Competition")
map_youth_status()

tableMarket()
# refreshButton()