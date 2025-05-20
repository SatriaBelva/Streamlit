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

        st.header(f"Kec. {selected_kecamatan} Desa {selected_desa}")
        st.caption("Rekomendasi")

        # Pertanyaan otomatis
        default_query =  f"""Berdasarkan data Kecamatan {selected_kecamatan}, Desa {selected_desa} termasuk kelompok usia dominan, 
        tingkat pendidikan, komposisi pekerjaan, kebiasaan penggunaan internet, dan tingkat ekonomi, berikan rekomedasi paket internet 
        {selected_Product} yang dipilih berdasarkan usia dominan dan kebiasaan mereka, dengan harga dan benefit menyesuaikan dengan 
        kategori ekonomi (rendah, menengah, tinggi) namun tetap menawarkan opsi terjangkau meski untuk ekonomi tinggi, disertai dengan alasan"""

        # Input pertanyaan manual dari user (di bawah)
        # st.markdown("### Ajukan pertanyaan lain:")
        user_query = st.chat_input("Tanyakan sesuatu tentang paket internet Telkomsel...")
        
        qa = load_chatbot_popu()
        
        if user_query and user_query.strip() != "":
            with st.spinner("Sedang mencari jawaban..."):
                result = get_chatbot_response_popu(qa, user_query)
                st.markdown("### Jawaban dari pertanyaan Anda:")
                st.markdown(result["result"])

        # Jika user tidak mengisi apapun, tampilkan default query
        elif user_query is None:
            with st.spinner("Sedang mencari jawaban..."):
                result = get_chatbot_response_popu(qa, default_query)
                st.markdown("### Rekomendasi Paket untuk Wilayah Ini:")
                st.markdown(result["result"])
                
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
            background: linear-gradient(to right, #FD9B2A, #E30511);
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