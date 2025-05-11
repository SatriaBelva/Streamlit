import streamlit as st
import pandas as pd
import numpy as np
import os as os
from controller import *
from model import *

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
        qa = load_chatbot_popu()

        # Pertanyaan otomatis
        default_query = f"Berikan beberapa rekomendasi pilihan paket internet {selected_Product} beserta harga dan benefitnya di kecamatan {selected_kecamatan} desa {selected_desa} berdasarkan jumlah penduduk, pendidikan dan pekerjaan yang ada disitu, dan berikan alasannya"

        with st.spinner("Sedang mencari jawaban..."):
            default_result = get_chatbot_response_popu(qa, default_query)
            st.markdown("### Jawaban dari pertanyaan otomatis:")
            st.markdown(default_result["result"])

        # Garis pemisah
        st.markdown("---")

        # Input pertanyaan manual dari user (di bawah)
        st.markdown("### Ajukan pertanyaan lain:")
        user_query = st.chat_input("Tanyakan sesuatu tentang paket internet Telkomsel...")

        if user_query:
            with st.spinner("Sedang mencari jawaban..."):
                user_result = get_chatbot_response_popu(qa, user_query)
                st.markdown("### Jawaban dari pertanyaan Anda:")
                st.markdown(user_result["result"])
            
st.title("Pendidikan")
graphPendidikan(st.session_state['kecamatan'])

st.title("Pekerjaan")
graphPekerjaan(st.session_state['kecamatan'])

st.title("Jumlah Penduduk")
graphJumlahPenduduk(st.session_state['kecamatan'])

st.title("Jumlah KK")
graphJumlahKK(st.session_state['kecamatan'])

tablePopultycs(st.session_state['kecamatan'])