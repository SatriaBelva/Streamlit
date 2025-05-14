import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
import altair as alt

# def graphIndeksEkonomi(kecamatan):
#     if kecamatan == "Semua" : 
#         dataPendidikan = pd.DataFrame(
#             {
#                 "Kecamatan"          : get_kecamatan_data()["nama"].tolist(),
#                 "Indeks Ekonomi"     : get_indeks_ekonomi(kecamatan)["Indeks Ekonomi"].tolist(),
#             }
#         )
#         st.bar_chart(dataPendidikan, x="Kecamatan", y="Indeks Ekonomi", horizontal=False, stack=True, color="#E30511", height=550)
#     elif kecamatan != "Semua" : 
#         dataPendidikan = pd.DataFrame(
#             {
#                 "Kecamatan"    : get_kecamatan_data()["nama"].tolist(),
#                 "Indeks Ekonomi"                            : get_indeks_ekonomi(kecamatan)["Indeks Ekonomi"].tolist()
#             }
#         )
#         st.bar_chart(dataPendidikan, x="Kecamatan", y="Indeks Ekonomi", horizontal=False, stack=True, color="#E30511", height=550)

def get_color(value):
    if value < 30:
        return '#E30511'
    elif 30 <= value < 60:
        return '#FD9B2A'
    else:
        return '#229122'

def graphIndeksEkonomi(kecamatan):
    if kecamatan == "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                "Kecamatan"          : get_kecamatan_data()["nama"].tolist(),
                "Indeks Ekonomi"     : get_indeks_ekonomi(kecamatan)["Indeks Ekonomi"].tolist(),
            }
        )
    elif kecamatan != "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                "Kecamatan"    : get_kecamatan_data()["nama"].tolist(),
                "Indeks Ekonomi"                            : get_indeks_ekonomi(kecamatan)["Indeks Ekonomi"].tolist()
            }
        )

    dataPendidikan["Warna"] = dataPendidikan["Indeks Ekonomi"].apply(get_color)

    # Chart dengan Altair
    chart = alt.Chart(dataPendidikan).mark_bar().encode(
        x=alt.X('Kecamatan:N', sort=None),
        y=alt.Y('Indeks Ekonomi:Q'),
        color=alt.Color('Warna:N', scale=None, legend=None),
        tooltip=['Kecamatan', 'Indeks Ekonomi']
    ).properties(
        height=550,
        width=900
    )

    st.altair_chart(chart, use_container_width=True)