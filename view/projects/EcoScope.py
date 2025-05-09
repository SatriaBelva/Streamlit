import streamlit as st
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
        # st.caption("Rekomendasi")

        # query = f"Bagaimana strategi pemasaran yang cocok untuk diterapkan di wilayah kecamatan {selected_kecamatan} berdasarkan tingkat ekonomi dan dengan pendapatan masyarakat yang ada disitu, dan berikan alasannya"
        # qa = load_chatbot_eco()

        # if query:
        #     with st.spinner("Sedang Mencari Jawaban"):
        #         result = get_chatbot_response_eco(qa, query)
        #         st.markdown(result["result"])
    # if st.session_state.kecamatan == "Search Kecamatan":
    #     st.warning("Silahkan Pilih Kecamatan Terlebih dahulu")
    # elif st.session_state.kecamatan == "Semua":
    #     with st.container(border=True, height=600):
    #         st.title(f"kec. {selected_kecamatan}")
    #         st.caption("Rekomendasi")

    #         query = f"Bagaimana strategi pemasaran yang cocok untuk diterapkan di wilayah kecamatan {selected_kecamatan} berdasarkan tingkat ekonomi dan dengan pendapatan masyarakat yang ada disitu, dan berikan alasannya"
    #         qa = load_chatbot()

    #         if query:
    #             with st.spinner("Sedang Mencari Jawaban"):
    #                 result = get_chatbot_response(qa, query)
    #                 st.markdown(result["result"])
    # elif st.session_state.kecamatan != "Semua":
    #     with st.container(border=True, height=600):
    #         st.title(f"Kabupaten Jember")
    #         st.title(f"kec. {selected_kecamatan}")
    #         st.caption("Rekomendasi")

    #         query = f"Bagaimana strategi pemasaran yang cocok untuk diterapkan di wilayah kecamatan {selected_kecamatan} berdasarkan tingkat ekonomi dan dengan pendapatan masyarakat yang ada disitu, dan berikan alasannya"
    #         qa = load_chatbot()

    #         if query:
    #             with st.spinner("Sedang Mencari Jawaban"):
    #                 result = get_chatbot_response(qa, query)
    #                 st.markdown(result["result"])

st.title("Indeks Ekonomi")
graphIndeksEkonomi(st.session_state['kecamatan'])

tableEcoscope(st.session_state['kecamatan'])