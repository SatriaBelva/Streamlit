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
    if kecamatan == "Semua":
        df = pd.DataFrame({
            "Kecamatan": get_kecamatan_data()["nama"].tolist(),
            "Indeks Ekonomi": get_indeks_ekonomi(kecamatan)["Indeks Ekonomi"].tolist(),
        })
    else:
        df = pd.DataFrame({
            "Kecamatan": get_kecamatan_data()["nama"].tolist(),
            "Indeks Ekonomi": get_indeks_ekonomi(kecamatan)["Indeks Ekonomi"].tolist(),
        })

    df["Warna"] = df["Indeks Ekonomi"].apply(get_color)

    # Bar chart
    bar = alt.Chart(df).mark_bar().encode(
        x=alt.X('Kecamatan:N', sort=None),
        y=alt.Y('Indeks Ekonomi:Q'),
        color=alt.Color('Warna:N', scale=None, legend=None),
        tooltip=['Kecamatan', 'Indeks Ekonomi']
    ).properties(height=550, width=900)

    # Text label di atas bar
    text = alt.Chart(df).mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        x=alt.X('Kecamatan:N'),
        y=alt.Y('Indeks Ekonomi:Q'),
        text=alt.Text('Indeks Ekonomi:Q', format=".1f")  # satu angka di belakang koma
    )

    st.altair_chart(bar + text, use_container_width=True)