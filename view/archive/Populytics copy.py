import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import os as os
from controller import *

if 'kecamatan' not in st.session_state:
    st.session_state['kecamatan'] = "Semua"
if 'desa' not in st.session_state:
    st.session_state['desa'] = "Semua"

gdf = map_path()
kecamatanList = kecamatan_list()

# Selectbox For Kecamatan and Desa
colKecamatan, colDesa, colEmpty = st.columns([0.25, 0.25, 0.5])
with colKecamatan:
    selected_kecamatan = st.selectbox("Pilih Kecamatan", ["Search Kecamatan"] + ["Semua"] + kecamatanList, index=0, key="kecamatan")
with colDesa:
    if selected_kecamatan != "Semua":
        desa_list = sorted(gdf[gdf['WADMKC'] == selected_kecamatan]['NAMOBJ'].unique())
    else:
        desa_list = sorted(gdf['NAMOBJ'].unique())
    selected_desa = st.selectbox("Pilih Desa", ["Search Desa"] + ["Semua"] + desa_list, index=0, key="desa")

# Div For Map and Recomendation
colMap, colText = st.columns([0.65, 0.35])
with colMap :
    map(st.session_state['kecamatan'], st.session_state['desa'])
    index_kecamatan = kecamatanList.index(st.session_state.get("kecamatan"))
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

# Div For Total Population Graph and It's Metric
colGraph, colMetrics = st.columns([0.65, 0.35], vertical_alignment='top')
with colGraph :
    jumlah_penduduk = pd.DataFrame({
        'Kecamatan' : kecamatanList,
        'Penduduk': np.random.randint(5000, 25000, size=len(kecamatanList))
    })
    st.bar_chart(
        jumlah_penduduk,
        x="Kecamatan",
        y="Penduduk",
        color='#B7242A',
        height=500
    )
with colMetrics :
    # with st.container(border=True, height=500) :
    if st.session_state.kecamatan == "Search Kecamatan" : 
        st.warning("Silahkan Pilih Kecamatan Terlebih dahulu")
    elif st.session_state.kecamatan == "Semua":
        st.metric(label=f"Jumlah Penduduk Kabupaten Jember", value=f'{jumlah_penduduk['Penduduk'][index_kecamatan]:,}', delta=f'1000', delta_color='normal', border=True)
        st.metric(label=f"Jumlah KK Kabupaten Jember", value = f"{jumlah_penduduk['Penduduk'][index_kecamatan] - 5000:,}", delta=f'1000', delta_color='normal', border=True)
    else :
        st.metric(label=f"Jumlah Penduduk Kecamatan {st.session_state['kecamatan']}", value=f'{jumlah_penduduk['Penduduk'][index_kecamatan]:,}', delta=f'1000', delta_color='normal', border=True)
        st.metric(label=f"Jumlah KK Kecamatan {st.session_state['kecamatan']}", value = f"{jumlah_penduduk['Penduduk'][index_kecamatan] - 5000:,}", delta=f'1000', delta_color='normal', border=True)

# Div For Pendidikan and Pekerjaan Metric
colPendidikan, colPekerjaan = st.columns(2, vertical_alignment='top')
with colPendidikan :
        st.header("Pendidikan")
        st.divider()
with colPekerjaan :
        st.header("Pekerjaan")
        st.divider()

if st.session_state.kecamatan == "Search Kecamatan" : 
    st.warning("Silahkan Pilih Kecamatan Terlebih dahulu")
else :
    with colPendidikan :
        pendidikanGraph, pendidikanMetric = st.columns(2)
        with pendidikanGraph :
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.area_chart(chart_data, height=408.667)
        with pendidikanMetric :
            st.metric(label=f"Jumlah Penduduk Tamatan SD", value=f'{jumlah_penduduk['Penduduk'][index_kecamatan]:,}', delta=f'39.11%', delta_color='normal')
            st.metric(label=f"Jumlah Penduduk Tamatan SLTP", value = f"{jumlah_penduduk['Penduduk'][index_kecamatan] - 5000:,}", delta=f'-28.02%', delta_color='normal')
            st.metric(label=f"Jumlah Penduduk Tamatan SLTA", value = f"{jumlah_penduduk['Penduduk'][index_kecamatan] - 5000:,}", delta=f'23.13%', delta_color='normal')
    with colPekerjaan :
        pendidikanGraph, pendidikanMetric = st.columns(2)
        with pendidikanGraph :
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.area_chart(chart_data, height=408.667)
        with pendidikanMetric :
            st.metric(label=f"Nelayan", value=f'{jumlah_penduduk['Penduduk'][index_kecamatan]:,}', delta=f'39.11%', delta_color='normal')
            st.metric(label=f"Petani", value = f"{jumlah_penduduk['Penduduk'][index_kecamatan] - 5000:,}", delta=f'-28.02%', delta_color='normal')
            st.metric(label=f"Perawat", value = f"{jumlah_penduduk['Penduduk'][index_kecamatan] - 5000:,}", delta=f'23.13%', delta_color='normal')

# Div For DataFrame Table
data = pd.DataFrame({
    'Kecamatan': kecamatanList,
    'Penduduk': np.random.randint(5000, 25000, size=len(kecamatanList)),
    'Pendidikan': np.random.randint(5000, 25000, size=len(kecamatanList)),
    'Status': ['Gagal'] * len(kecamatanList)
})

rows_per_page = 10
total_pages = len(data) // rows_per_page + (1 if len(data) % rows_per_page > 0 else 0)

if 'page' not in st.session_state:
    st.session_state.page = 1

start_idx = (st.session_state.page - 1) * rows_per_page
end_idx = start_idx + rows_per_page
current_data = data.iloc[start_idx:end_idx]

st.dataframe(current_data, use_container_width=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    pass
with col2:
    if st.button("⬅️ Prev", key="prev_button", use_container_width=True, ) and st.session_state.page > 1:
        st.session_state.page -= 1
        st.rerun()
with col3:
    st.markdown(
        f"<div style='text-align: center; font-weight: normal; padding-top:6px;'>Page {st.session_state.page} of {total_pages}</div>",
        unsafe_allow_html=True
    )   
with col4:
    if st.button("Next ➡️", key="next_button", use_container_width=True) and st.session_state.page < total_pages:
        st.session_state.page += 1
        st.rerun()
with col5:
    pass