import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import os as os
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
image_path = r"D:\magang telkom 2\Streamlit\assets\foto_telkom_katanya.png"
img_base64 = image_to_base64(image_path)

# Styling header dan layout
st.markdown("""
    <style>
        .main > div:first-child {
            padding-top: 0rem;
        }

        .custom-header-container {
            background-color: #D70000;
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
            height: 135px;

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
            <div class="custom-header-title">Populitycs Kabupaten Jember</div>
            <div class="custom-header-subtitle">Data pada fitur ini merupakan data IPM Kabupaten<br>Jember</div>
        </div>
    </div>
""", unsafe_allow_html=True)


if 'kecamatan' not in st.session_state:
    st.session_state['kecamatan'] = "Semua"
if 'desa' not in st.session_state:
    st.session_state['desa'] = "Semua"

gdf = map_path()
kecamatanList = kecamatan_list()

# Selectbox For Kecamatan and Desa
colKecamatan, colDesa = st.columns([0.65, 0.35])
with colKecamatan:
    selected_kecamatan = st.selectbox("Pilih Kecamatan", ["Semua"] + kecamatanList, index=0, key="kecamatan")
with colDesa:
    pass

# Div For Map and Recomendation
colMap, colText = st.columns([0.65, 0.35])
with colMap :
    mapEcoscope(st.session_state['kecamatan'])
    index_kecamatan = kecamatanList.index(st.session_state.get("kecamatan"))
    # pass
with colText :
    with st.container(border=True, height=600):
        st.title(f"kec. {selected_kecamatan}")
        st.caption("Rekomendasi")
        
        default_query = f"Bagaimana strategi pemasaran yang cocok untuk diterapkan di wilayah kecamatan {selected_kecamatan} berdasarkan tingkat ekonomi dan dengan pendapatan masyarakat yang ada disitu, dan berikan alasannya"

        # Input pertanyaan manual dari user (di bawah)
        # st.markdown("### Ajukan pertanyaan lain:")
        user_query = st.chat_input("Tanyakan sesuatu tentang paket internet Telkomsel...")

        # qa = load_chatbot_eco()
        # with st.spinner("Sedang mencari jawaban..."):
        #     default_result = get_chatbot_response_eco(qa, default_query)
        #     st.markdown(default_result["result"])

        # # Garis pemisah
        # st.markdown("---")

        # final_query = user_query if user_query.strip() != "" else default_query


        # if final_query:
        #     with st.spinner("Sedang mencari jawaban..."):
        #         user_result = get_chatbot_response_eco(qa, final_query)
        #         st.markdown("### Jawaban dari pertanyaan Anda:")
        #         st.markdown(user_result["result"])
with st.container(border=True):
    st.title("Indeks Ekonomi")
    graphIndeksEkonomi(st.session_state['kecamatan'])

tableEcoscope(st.session_state['kecamatan'])