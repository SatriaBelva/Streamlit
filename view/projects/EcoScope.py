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
            <div class="custom-header-title">EcoScope Kabupaten Jember</div>
            <div class="custom-header-subtitle">Data ini menunjukkan tingkat ekonomi di Kabupaten Jember, dihitung dari Indeks Ekonomi tiap kecamatan yang didapat dengan mengalikan jumlah pekerja dengan bobot jenis pekerjaannya, membaginya dengan total penduduk, lalu dinormalisasi ke skala 0–100.</div>
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
        st.header(f"Kec. {selected_kecamatan}")
        st.caption("Rekomendasi")
        
        # default_queryeco = f"Berikan tiga strategi pemasaran yang cocok diterapkan di wilayah kecamatan {selected_kecamatan} berdasarkan nilai IPM dan tingkat pendapatan masyarakat, dengan membedakan antara masyarakat yang tidak bekerja, masyarakat dengan pendapatan tidak stabil, dan masyarakat dengan pendapatan stabil. Berikan alasannya untuk masing-masing strategi"      
        # user_queryeco = st.chat_input("Tanyakan sesuatu tentang paket internet Telkomsel...")
        
        # qa = None
        
        # if user_queryeco and user_queryeco.strip() != "":
        #     with st.spinner("Sedang mencari jawaban..."):
        #         result = get_chatbot_response_eco(user_queryeco)
        #         st.markdown("### Jawaban dari pertanyaan Anda:")
        #         st.markdown(result, unsafe_allow_html=True)

        # # Jika user tidak mengisi apapun, tampilkan default query
        # elif user_queryeco is None:
        #     with st.spinner("Sedang mencari jawaban..."):
        #         result = get_chatbot_response_eco(default_queryeco)
        #         st.markdown("### Rekomendasi Paket untuk Wilayah Ini:")
        #         st.markdown(result, unsafe_allow_html=True)
    # with st.container(border=True, height=600):
    #     st.header(f"Kec. {selected_kecamatan}")
    #     st.caption("Rekomendasi")
        
    #     default_queryeco = f"Berikan tiga strategi pemasaran yang cocok diterapkan di wilayah kecamatan {selected_kecamatan} berdasarkan nilai IPM dan tingkat pendapatan masyarakat, dengan membedakan antara masyarakat yang tidak bekerja, masyarakat dengan pendapatan tidak stabil, dan masyarakat dengan pendapatan stabil. Berikan alasannya untuk masing-masing strategi"      
    #     user_queryeco = st.chat_input("Tanyakan sesuatu tentang paket internet Telkomsel...")
        
    #     embedder, index, documents = load_chatbot_eco()

    #     if user_queryeco and user_queryeco.strip() != "":
    #         with st.spinner("Sedang mencari jawaban..."):
    #             resulteco = get_chatbot_response_eco(embedder, index, documents, user_queryeco)
    #             st.markdown("### Jawaban dari pertanyaan Anda:")
    #             st.markdown(resulteco["result"])

    #     # Jika user tidak mengisi apapun, tampilkan default query
    #     elif user_queryeco is None:
    #         with st.spinner("Sedang mencari jawaban..."):
    #             resulteco = get_chatbot_response_eco(embedder, index, documents, default_queryeco)
    #             st.markdown("### Strategi untuk Wilayah Ini:")
    #             st.markdown(resulteco["result"])

with st.container(border=True):
    st.title("Indeks Ekonomi")
    graphIndeksEkonomi(st.session_state['kecamatan'])

tableEcoscope(st.session_state['kecamatan'])