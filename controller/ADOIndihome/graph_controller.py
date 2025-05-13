import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
import altair as alt
import plotly_express as px

def graph_ListAktif_TotalHousehold():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten"            : get_Kabupaten_data(),
            "List Aktif"           : get_ListAktif_data(),
            "List Non Aktif"       : get_ListNonAktif_data(),
        }
    )

    dataPendidikan["List Aktif"] = (
        dataPendidikan["List Aktif"]
        .astype(str)
        .str.replace(".", "", regex=False)  # hapus titik ribuan
        .str.replace(",", "", regex=False)  # jaga-jaga kalau ada koma
        .astype(int)  # gunakan int, bukan float
    )

    dataPendidikan["List Non Aktif"] = (
        dataPendidikan["List Non Aktif"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(int)
    )

    df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars=["List Aktif", "List Non Aktif"], var_name="Kategori", value_name="Jumlah")

    chart = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X("Kabupaten:N", sort=None),
        y=alt.Y("Jumlah:Q"),
        # xOffset="Kategori:N",  # Buat Ngatur Stack
        color=alt.Color("Kategori:N", scale=alt.Scale(range=["#E30511", "#F5868D"]), legend=alt.Legend(orient="top")),  # 👈 legend di bawah),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ]
    ).properties(height=550)

    return st.altair_chart(chart, use_container_width=True)

def graph_PortAvail_TotalPort():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten"            : get_Kabupaten_data(),
            "Port Available"       : get_PortAvail_data(),
            "Port Unavailable"     : get_PortUnavail_data(),
        }
    )

    dataPendidikan["Port Available"] = (
        dataPendidikan["Port Available"]
        .astype(str)
        .str.replace(".", "", regex=False)  # hapus titik ribuan
        .str.replace(",", "", regex=False)  # jaga-jaga kalau ada koma
        .astype(int)  # gunakan int, bukan float
    )

    dataPendidikan["Port Unavailable"] = (
        dataPendidikan["Port Unavailable"]
        .astype(str)
        .str.replace(".", "", regex=False)  # hapus titik ribuan
        .str.replace(",", "", regex=False)  # jaga-jaga kalau ada koma
        .astype(int)  # gunakan int, bukan float
    )


    df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars=["Port Available", "Port Unavailable"], var_name="Kategori", value_name="Jumlah")

    chart = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X("Kabupaten:N", sort=None),
        y=alt.Y("Jumlah:Q"),
        # xOffset="Kategori:N",  # Ini penting untuk grouped bar
        color=alt.Color("Kategori:N", scale=alt.Scale(range=["#E30511","#F5868D"]), legend=alt.Legend(orient="top")),  # 👈 legend di bawah),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ]
    ).properties(height=550)
    return st.altair_chart(chart, use_container_width=True)

# def graph_WifiShare():
#     dataPendidikan = pd.DataFrame(
#         {
#             "Kabupaten"     : get_Kabupaten_data(),
#             "Wifi Share"    : get_WifiShare_data(),
#         }
#     )
#     # Bersihkan dan ubah koma jadi titik, lalu ubah ke float
#     dataPendidikan["Wifi Share"] = (dataPendidikan["Wifi Share"].astype(str).str.replace(",", ".", regex=False).astype(float))

#     df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars="Wifi Share", var_name="Kategori", value_name="Jumlah")

#     chart = alt.Chart(df_melted).mark_bar().encode(
#         x=alt.X("Kabupaten:N", sort=None),
#         y=alt.Y("Jumlah:Q"),
#         # xOffset="Kategori:N",  # Ini penting untuk grouped bar
#         color=alt.Color("Kategori:N", scale=alt.Scale(range=["#E30511","#F5868D"]), legend=alt.Legend(orient="bottom")),  # 👈 legend di bawah),
#         tooltip=[
#             alt.Tooltip("Kabupaten:N"),
#             alt.Tooltip("Kategori:N"),
#             alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
#         ]
#     ).properties(height=550)

#     return st.altair_chart(chart, use_container_width=True)

# def graph_ODP():
#     dataPendidikan = pd.DataFrame(
#         {
#             "Kabupaten" : get_Kabupaten_data(),
#             "ODP"       : get_ODP_data(),
#         }
#     )
    
#     dataPendidikan["ODP"] = (
#         dataPendidikan["ODP"]
#         .astype(str)
#         .str.replace(",", ".", regex=False)  # ubah koma ke titik
#         .astype(float)
#     )

#     df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars="ODP", var_name="Kategori", value_name="Jumlah")

#     chart = alt.Chart(df_melted).mark_bar().encode(
#         x=alt.X("Kabupaten:N", sort=None),
#         y=alt.Y("Jumlah:Q"),
#         # xOffset="Kategori:N",  # Ini penting untuk grouped bar
#         color=alt.Color("Kategori:N", scale=alt.Scale(range=["#E30511","#F5868D"]), legend=alt.Legend(orient="bottom")),  # 👈 legend di bawah),
#         tooltip=[
#             alt.Tooltip("Kabupaten:N"),
#             alt.Tooltip("Kategori:N"),
#             alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
#         ]
#     ).properties(height=550)

#     return st.altair_chart(chart, use_container_width=True)


def graph_WifiShare_pie():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten"     : get_Kabupaten_data(),
            "Wifi Share"    : get_WifiShare_data(),
        }
    )
    # Bersihkan dan ubah koma jadi titik, lalu ubah ke float
    dataPendidikan["Wifi Share"] = (dataPendidikan["Wifi Share"].astype(str).str.replace(",", ".", regex=False).astype(float))

    fig = px.pie(
        dataPendidikan,
        values="Wifi Share",
        names="Kabupaten",
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    st.plotly_chart(fig, use_container_width=True)

def graph_ODP_pie():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten" : get_Kabupaten_data(),
            "ODP"       : get_ODP_data(),
        }
    )
    
    dataPendidikan["ODP"] = (
        dataPendidikan["ODP"]
        .astype(str)
        .str.replace(",", ".", regex=False)  # ubah koma ke titik
        .astype(float)
    )
    fig = px.pie(
        dataPendidikan,
        values="ODP",
        names="Kabupaten",
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    st.plotly_chart(fig, use_container_width=True)