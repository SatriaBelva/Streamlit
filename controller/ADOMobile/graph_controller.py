import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
import altair as alt
import plotly_express as px

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
        # xOffset="Kategori:N",  # Ini penting untuk grouped bar
        color=alt.Color("Kategori:N", scale=alt.Scale(range=["#FD9B2A", "#E30511"]), legend=alt.Legend(orient="top")),  # 👈 legend di bawah),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ]
    ).properties(height=550)
    
    text = alt.Chart(df_melted).mark_text(
        align="center",
        baseline="bottom",
        dy=-5,
        color="black"
    ).encode(
        x=alt.X("Kabupaten:N", sort=None),
        y=alt.Y("Jumlah:Q", stack="zero"),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ],
        text=alt.Text("Jumlah:Q", format=","),
        detail="Kategori:N"
    )

    return st.altair_chart(chart + text, use_container_width=True)

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
        color=alt.Color("Kategori:N", scale=alt.Scale(range=["#E30511", "#FD9B2A"]), legend=alt.Legend(orient="top")),  # 👈 legend di bawah),
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ]
    ).properties(height=550)
    
    text = (
        alt.Chart(df_melted)
        .mark_text(
            dy=-5,  # sedikit naik di atas bar
            color="black",
            align="center",
            baseline="bottom",
            size=12,
        )
        .encode(
            x=alt.X("Kabupaten:N", sort=None),
            y=alt.Y("Jumlah:Q"),
            tooltip=[
                alt.Tooltip("Kabupaten:N"),
                alt.Tooltip("Kategori:N"),
                alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
            ],
            text=alt.Text("Jumlah:Q", format=".2f"),  # format angka dengan 2 desimal
            xOffset="Kategori:N",
        )
    )

    return st.altair_chart(chart + text, use_container_width=True)
    
def graph_OUTLETPJP():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten": get_Kabupaten_data(),
            "OUTLET PJP": get_OUTLETPJP_data(),
        }
    )

    df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars="OUTLET PJP", var_name="Kategori", value_name="Jumlah")

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
    text = alt.Chart(df_melted).mark_text(
        align="center", baseline="bottom", dy=-5
    ).encode(
        x=alt.X("Kabupaten:N"),
        y="Jumlah:Q",
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ],
        text=alt.Text("Jumlah:Q", format=",")  # format angka ribuan
    )

    return st.altair_chart(chart + text, use_container_width=True)
# def graph_OUTLETPJP_pie():
#     dataPendidikan = pd.DataFrame(
#         {
#             "Kabupaten": get_Kabupaten_data(),
#             "OUTLET PJP": get_OUTLETPJP_data(),
#         }
#     )

#     fig = px.pie(
#         dataPendidikan,
#         values="OUTLET PJP",
#         names="Kabupaten",
#         color_discrete_sequence=px.colors.sequential.RdBu
#     )

#     st.plotly_chart(fig, use_container_width=True)

# def graph_Arpu():
#     dataPendidikan = pd.DataFrame(
#         {
#             "Kabupaten" : get_Kabupaten_data(),
#             "ARPU"      : get_Arpu_data(),
#         }
#     )

#     # Misalnya mau ditampilkan dalam chart:
#     chart = alt.Chart(dataPendidikan).mark_bar().encode(
#         x=alt.X("Kabupaten:N", sort=list(dataPendidikan["Kabupaten"])),
#         y=alt.Y("ARPU:Q"),
#         color=alt.value("#E30511"),
#         tooltip=[
#             alt.Tooltip("Kabupaten:N"),
#             alt.Tooltip("ARPU:Q", format=","),
#         ]
#     ).properties(height=550)

#     return st.altair_chart(chart, use_container_width=True)

def graph_Arpu():
    dataPendidikan = pd.DataFrame({
        "Kabupaten": get_Kabupaten_data(),
        "ARPU": get_Arpu_data(),
    })
    # dataPendidikan["Wifi Share"] = (dataPendidikan["Wifi Share"].astype(str).str.replace(",", ".", regex=False).astype(float))

    df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars="ARPU", var_name="Kategori", value_name="Jumlah")

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
    text = alt.Chart(df_melted).mark_text(
        align="center", baseline="bottom", dy=-5
    ).encode(
        x=alt.X("Kabupaten:N"),
        y="Jumlah:Q",
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ],
        text=alt.Text("Jumlah:Q", format=",")  # format angka ribuan
    )

    return st.altair_chart(chart + text, use_container_width=True)

def graph_Site():
    dataPendidikan = pd.DataFrame(
        {
            "Kabupaten" : get_Kabupaten_data(),
            "SITE"      :  get_Site_data(),
        }
    )
    df_melted = dataPendidikan.melt(id_vars="Kabupaten", value_vars="SITE", var_name="Kategori", value_name="Jumlah")

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
    text = alt.Chart(df_melted).mark_text(
        align="center", baseline="bottom", dy=-5
    ).encode(
        x=alt.X("Kabupaten:N"),
        y="Jumlah:Q",
        tooltip=[
            alt.Tooltip("Kabupaten:N"),
            alt.Tooltip("Kategori:N"),
            alt.Tooltip("Jumlah:Q", format=",")  # format angka ribuan
        ],
        text=alt.Text("Jumlah:Q", format=",")  # format angka ribuan
    )

    return st.altair_chart(chart + text, use_container_width=True)
# def graph_Site_pie():
#     dataPendidikan = pd.DataFrame(
#         {
#             "Kabupaten" : get_Kabupaten_data(),
#             "SITE"      :  get_Site_data(),
#         }
#     )

#     fig = px.pie(
#         dataPendidikan,
#         values="SITE",
#         names="Kabupaten",
#         color_discrete_sequence=px.colors.sequential.RdBu
#     )

#     st.plotly_chart(fig, use_container_width=True)

    
