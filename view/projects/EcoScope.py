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
    if st.session_state.kecamatan == "Search Kecamatan":
        st.warning("Silahkan Pilih Kecamatan Terlebih dahulu")
    elif st.session_state.kecamatan == "Semua":
        with st.container(border=True, height=600):
            st.title(f"Kabupaten Jember")
            st.caption(f'Indeks Pembangunan Manusia tergolong tinggi')
            st.write(f'Rekomendasi :\n\nLorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.')
    elif st.session_state.kecamatan != "Search Kecamatan" and st.session_state.kecamatan != "Semua":
        with st.container(border=True, height=600):
            st.title(f"Kec. {st.session_state.kecamatan}")
            st.caption(f'Indeks Pembangunan Manusia tergolong tinggi')
            st.write(f'Rekomendasi :\n\nLorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat magnam provident, consequatur pariatur itaque tempore aspernatur voluptate recusandae deserunt odit earum optio in illo atque possimus ipsam sequi voluptatum magni.')   

st.title("Indeks Ekonomi")
graphIndeksEkonomi(st.session_state['kecamatan'])

tableEcoscope(st.session_state['kecamatan'])