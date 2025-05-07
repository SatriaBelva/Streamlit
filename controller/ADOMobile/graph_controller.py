import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
import altair as alt

def graphCB_Populasi():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten" : get_Kabupaten_data(),
            "CB"        : get_CB_data(),
            "Populasi"  : get_Populasi_data(),
        }
    )

    dataPendidikan["CB"] = (
        dataPendidikan["CB"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )
    dataPendidikan["Populasi"] = (
        dataPendidikan["Populasi"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars=["CB", "Populasi"], var_name="Kategori", value_name="Jumlah")

    chart = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X("Kabupaten:N", sort=None),
        y=alt.Y("Jumlah:Q"),
        xOffset="Kategori:N",  # Ini penting untuk grouped bar
        color=alt.Color("Kategori:N", scale=alt.Scale(range=["#E30511", "#F5868D"]), legend=alt.Legend(orient="bottom")),  # 👈 legend di bawah),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ]
    ).properties(height=550)

    st.altair_chart(chart, use_container_width=True)

def graph_FBREG_FBYouth():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten"       : get_Kabupaten_data(),
            "FB Share REG"    : get_FBShareREG_data(),
            "FB Share Youth"  : get_FBShareYouth_data(),
        }
    )

    dataPendidikan["FB Share REG"] = (dataPendidikan["FB Share REG"].astype(str).str.replace(",", ".", regex=False).astype(float))
    dataPendidikan["FB Share Youth"] = (dataPendidikan["FB Share Youth"].astype(str).str.replace(",", ".", regex=False).astype(float))

    df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars=["FB Share REG", "FB Share Youth"], var_name="Kategori", value_name="Jumlah")

    chart = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X("Kabupaten:N", sort=None),
        y=alt.Y("Jumlah:Q"),
        xOffset="Kategori:N",  # Ini penting untuk grouped bar
        color=alt.Color("Kategori:N", scale=alt.Scale(range=["#E30511", "#F5868D"]), legend=alt.Legend(orient="bottom")),  # 👈 legend di bawah),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ]
    ).properties(height=550)

    return st.altair_chart(chart, use_container_width=True)
    
def graph_OUTLETPJP():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten": get_Kabupaten_data(),
            "OUTLET PJP": get_OUTLETPJP_data(),
        }
    )

    # Misalnya mau ditampilkan dalam chart:
    chart = alt.Chart(dataPendidikan).mark_bar().encode(
        x=alt.X("Kabupaten:N", sort=list(dataPendidikan["Kabupaten"])),
        y=alt.Y("OUTLET PJP:Q"),
        color=alt.value("#E30511"),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("OUTLET PJP:Q", format=","),
        ]
    ).properties(height=550)

    return st.altair_chart(chart, use_container_width=True)

def graph_Arpu():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten" : get_Kabupaten_data(),
            "ARPU"      : get_Arpu_data(),
        }
    )

    # Misalnya mau ditampilkan dalam chart:
    chart = alt.Chart(dataPendidikan).mark_bar().encode(
        x=alt.X("Kabupaten:N", sort=list(dataPendidikan["Kabupaten"])),
        y=alt.Y("ARPU:Q"),
        color=alt.value("#E30511"),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("ARPU:Q", format=","),
        ]
    ).properties(height=550)

    return st.altair_chart(chart, use_container_width=True)

def graph_Site():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten" : get_Kabupaten_data(),
            "SITE"      :  get_Site_data(),
        }
    )

    # Misalnya mau ditampilkan dalam chart:
    chart = alt.Chart(dataPendidikan).mark_bar().encode(
        x=alt.X("Kabupaten:N", sort=list(dataPendidikan["Kabupaten"])),
        y=alt.Y("SITE:Q"),
        color=alt.value("#E30511"),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("SITE:Q", format=","),
        ]
    ).properties(height=550)

    return st.altair_chart(chart, use_container_width=True)

    
