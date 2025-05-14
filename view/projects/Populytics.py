import streamlit as st
import pandas as pd
import numpy as np
import os as os
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
        <div class="custom-header-title">Populitycs Kabupaten Jember</div>
        <div class="custom-header-subtitle">Data pada fitur ini merupakan data IPM Kabupaten Jember</div>
    </div>
""", unsafe_allow_html=True)


if 'kecamatan' not in st.session_state:
    st.session_state['kecamatan'] = "Semua"
if 'desa' not in st.session_state:
    st.session_state['desa'] = "Semua"

gdf = map_path()
kecamatanList = kecamatan_list()
productList = ['Semua Produk', 'IndiHome', 'Telkomsel One', 'Telkomsel Prabayar', 'Telkomsel Orbit', 'Telkomsel Lite', 'Telkomsel by. U']

# Selectbox For Kecamatan and Desa
colKecamatan, colDesa, colProduct, colEmpty = st.columns([0.25, 0.25, 0.25, 0.5])
with colKecamatan:
    selected_kecamatan = st.selectbox("Pilih Kecamatan", ["Semua"] + kecamatanList, index=0, key="kecamatan")
with colDesa:
    if selected_kecamatan != "Semua":
        desa_list = sorted(gdf[gdf['WADMKC'] == selected_kecamatan]['NAMOBJ'].unique())
    else:
        desa_list = sorted(gdf['NAMOBJ'].unique())
    selected_desa = st.selectbox("Pilih Desa", ["Semua"] + desa_list, index=0, key="desa")
with colProduct:
    selected_Product = st.selectbox("Pilih Produk", productList, index=0, key="product")

# Div For Map and Recomendation
colMap, colText = st.columns([0.65, 0.35])
with colMap :
    # pass
    map(st.session_state['kecamatan'], st.session_state['desa'])
    index_kecamatan = kecamatanList.index(st.session_state.get("kecamatan"))
with colText :
    with st.container(border=True, height=600):

        st.title(f"kec. {selected_kecamatan} desa {selected_desa}")
        st.caption("Rekomendasi")

        # Pertanyaan otomatis
        default_query = f"Berikan beberapa rekomendasi pilihan paket internet {selected_Product} beserta harga dan benefitnya di kecamatan {selected_kecamatan} desa {selected_desa} berdasarkan jumlah penduduk, pendidikan dan pekerjaan yang ada disitu, dan berikan alasannya"

        # Input pertanyaan manual dari user (di bawah)
        # st.markdown("### Ajukan pertanyaan lain:")
        user_query = st.chat_input("Tanyakan sesuatu tentang paket internet Telkomsel...")
        
        # qa = load_chatbot_popu()
        
        # with st.spinner("Sedang mencari jawaban..."):
        #     default_result = get_chatbot_response_popu(qa, default_query)
        #     st.markdown(default_result["result"])

        # # Garis pemisah
        # st.markdown("---")

        # final_query = user_query if user_query.strip() != "" else default_query


        # if final_query:
        #     with st.spinner("Sedang mencari jawaban..."):
        #         user_result = get_chatbot_response_popu(qa, final_query)
        #         st.markdown("### Jawaban dari pertanyaan Anda:")
        #         st.markdown(user_result["result"])
with st.container(border=True):            
    st.title("Pendidikan")
    graphPendidikan(st.session_state['kecamatan'])
with st.container(border=True):
    st.title("Pekerjaan")
    graphPekerjaan(st.session_state['kecamatan'])
with st.container(border=True):
    st.title("Jumlah Penduduk")
    graphJumlahPenduduk(st.session_state['kecamatan'])
with st.container(border=True):
    st.title("Jumlah KK")
    graphJumlahKK(st.session_state['kecamatan'])


st.markdown("""
    <style>
        /* Header container */
        .custom-header2-container {
            background-color: #D70000;
            border-radius: 8px 80px 8px 80px;
            height: 135px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            margin-top: 1rem;
            margin-bottom: 2rem;
        }

        .custom-header2-subtitle {
            font-size: 16px;
            text-align: center;
            width: 80%;
            font-weight: normal;
            margin: 0;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Tampilkan header
st.markdown("""
    <div class="custom-header2-container">
        <div class="custom-header2-subtitle"> (i) Data pekerjaan dan pendidikan dibagi menjadi beberapa kategori. Untuk kategori data pekerjaan, tidak atau belum bekerja (pelajar, mahasiswa, IRT, pensiunan), memiliki penghasilan tidak stabil (pedagang, wiraswasta, nelayan), atau penghasilan stabil (guru, perawat, pengacara). Untuk kategori data pendidikan, tingkatannya meliputi sekolah tinggi (D1–S3), sekolah menengah (SLTP/SLTA), serta tamat SD, putus sekolah, atau tidak sekolah.</div>
    </div>
""", unsafe_allow_html=True)


tablePopultycs(st.session_state['kecamatan'])