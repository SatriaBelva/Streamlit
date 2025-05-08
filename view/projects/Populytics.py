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
    st.title(f"kec. {selected_kecamatan} desa {selected_desa}")
    st.caption("Rekomendasi")

    query = f"Berikan rekomendasi pilihan paket internet pada {selected_Product} di kecamatan {selected_kecamatan} desa {selected_desa} berdasarkan jumlah penduduk, pendidikan dan pekerjaan sesuai dengan tingkat ekonomi yang ada disitu, dan berikan alasannya"
    qa = load_chatbot()

    if query:
        with st.spinner("Sedang Mencari Jawaban"):
            result = get_chatbot_response(qa, query)
            st.markdown(result["result"])
    # if st.session_state.kecamatan == "Search Kecamatan":
    #     st.warning("Silahkan Pilih Kecamatan Terlebih dahulu")
    # elif st.session_state.kecamatan == "Semua":
    #     with st.container(border=True, height=600):
    #         st.title(f"kec. {selected_kecamatan} desa {selected_desa}")
    #         st.caption("Rekomendasi")

    #         query = f"Berikan rekomendasi pilihan paket internet pada {selected_Product} di kecamatan {selected_kecamatan} desa {selected_desa} berdasarkan jumlah penduduk, pendidikan dan pekerjaan sesuai dengan tingkat ekonomi yang ada disitu, dan berikan alasannya"
    #         qa = load_chatbot()

    #         if query:
    #             with st.spinner("Sedang Mencari Jawaban"):
    #                 result = get_chatbot_response(qa, query)
    #                 st.markdown(result["result"])
    # elif st.session_state.kecamatan != "Semua":
    #     with st.container(border=True, height=600):
    #         st.title(f"kec. {selected_kecamatan} desa {selected_desa}")
    #         st.caption("Rekomendasi")

    #         query = f"Berikan rekomendasi pilihan paket internet pada {selected_Product} di kecamatan {selected_kecamatan} desa {selected_desa} berdasarkan jumlah penduduk, pendidikan dan pekerjaan sesuai dengan tingkat ekonomi yang ada disitu, dan berikan alasannya"
    #         qa = load_chatbot()

    #         if query:
    #             with st.spinner("Sedang Mencari Jawaban"):
    #                 result = get_chatbot_response(qa, query)
    #                 st.markdown(result["result"])
            
st.title("Pendidikan")
graphPendidikan(st.session_state['kecamatan'])

st.title("Pekerjaan")
graphPekerjaan(st.session_state['kecamatan'])

st.title("Jumlah Penduduk")
graphJumlahPenduduk(st.session_state['kecamatan'])

st.title("Jumlah KK")
graphJumlahKK(st.session_state['kecamatan'])

tablePopultycs(st.session_state['kecamatan'])