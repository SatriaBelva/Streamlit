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

def get_color_label_indeksEkonomi(value):
    if value <= 40:
        return 'Rendah'
    elif 41 <= value < 70:
        return 'Sedang'
    else:
        return 'Tinggi'

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

    # Tambahkan label kategori dan warna
    df["Kategori"] = df["Indeks Ekonomi"].apply(get_color_label_indeksEkonomi)
    warna_dict = {
        "Rendah": "#E30511", "Sedang": "#FD9B2A", "Tinggi": "#229122"
    }

    # Bar chart dengan warna dan legend
    bar = alt.Chart(df).mark_bar().encode(
        x=alt.X('Kecamatan:N', sort=None),
        y=alt.Y('Indeks Ekonomi:Q'),
        color=alt.Color('Kategori:N',
                        scale=alt.Scale(domain=list(warna_dict.keys()), range=list(warna_dict.values())),
                        legend=alt.Legend(orient="top")),
        tooltip=['Kecamatan', 'Indeks Ekonomi', 'Kategori']
    ).properties(height=550, width=900)

    # Text label
    text = alt.Chart(df).mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        x=alt.X('Kecamatan:N'),
        y=alt.Y('Indeks Ekonomi:Q'),
        tooltip=['Kecamatan', 'Indeks Ekonomi', 'Kategori'],
        text=alt.Text('Indeks Ekonomi:Q', format=".1f")
    )

    st.altair_chart(bar + text, use_container_width=True)



def get_color_label_dayaBeli(value):
    if value <= 50000000000:
        return 'Rendah'
    elif 50000000001 <= value < 100000000000:
        return 'Sedang'
    else:
        return 'Tinggi'

def graphDayaBeli(kecamatan):
    if kecamatan == "Semua":
        df = pd.DataFrame({
            "Kecamatan": get_kecamatan_data()["nama"].tolist(),
            "Daya Beli/ Kecamatan": get_DayaBeli(kecamatan)["Daya Beli/ Kecamatan"].tolist(),
        })
    else:
        df = pd.DataFrame({
            "Kecamatan": get_kecamatan_data()["nama"].tolist(),
            "Daya Beli/ Kecamatan": get_DayaBeli(kecamatan)["Daya Beli/ Kecamatan"].tolist(),
        })

    # Tambahkan label kategori dan warna
    df["Kategori"] = df["Daya Beli/ Kecamatan"].apply(get_color_label_dayaBeli)
    warna_dict = {
        "Rendah": "#E30511", "Sedang": "#FD9B2A", "Tinggi": "#229122"
    }

    # Bar chart dengan warna dan legend
    bar = alt.Chart(df).mark_bar().encode(
        x=alt.X('Kecamatan:N', sort=None),
        y=alt.Y('Daya Beli/ Kecamatan:Q'),
        color=alt.Color('Kategori:N',
                        scale=alt.Scale(domain=list(warna_dict.keys()), range=list(warna_dict.values())),
                        legend=alt.Legend(orient="top")),
        tooltip=['Kecamatan', 'Daya Beli/ Kecamatan', 'Kategori']
    ).properties(height=550, width=900)

    # Text label
    text = alt.Chart(df).mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        x=alt.X('Kecamatan:N'),
        y=alt.Y('Daya Beli/ Kecamatan:Q'),
        tooltip=['Kecamatan', 'Daya Beli/ Kecamatan', 'Kategori'],
        text=alt.Text('Daya Beli/ Kecamatan:Q', format=".1f")
    )

    st.altair_chart(bar + text, use_container_width=True)