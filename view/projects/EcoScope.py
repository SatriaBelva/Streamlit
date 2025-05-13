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
        st.caption("Rekomendasi")
        qa = load_chatbot_eco()

        default_query = f"Bagaimana strategi pemasaran yang cocok untuk diterapkan di wilayah kecamatan {selected_kecamatan} berdasarkan tingkat ekonomi dan dengan pendapatan masyarakat yang ada disitu, dan berikan alasannya"

        # Input pertanyaan manual dari user (di bawah)
        # st.markdown("### Ajukan pertanyaan lain:")
        user_query = st.chat_input("Tanyakan sesuatu tentang paket internet Telkomsel...")

        with st.spinner("Sedang mencari jawaban..."):
            default_result = get_chatbot_response_eco(qa, default_query)
            st.markdown(default_result["result"])

        # Garis pemisah
        st.markdown("---")

        final_query = user_query if user_query.strip() != "" else default_query


        if final_query:
            with st.spinner("Sedang mencari jawaban..."):
                user_result = get_chatbot_response_eco(qa, final_query)
                st.markdown("### Jawaban dari pertanyaan Anda:")
                st.markdown(user_result["result"])

st.title("Indeks Ekonomi")
graphIndeksEkonomi(st.session_state['kecamatan'])

tableEcoscope(st.session_state['kecamatan'])