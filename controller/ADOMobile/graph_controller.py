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


def get_color_label_dayaBelimob(value):
    if value <= 1000000000000:
        return 'Rendah'
    elif 1000000000001 <= value <= 2000000000000: # Saya perbaiki logikanya menjadi <=
        return 'Sedang'
    else:
        return 'Tinggi'

    
def graphDayaBelimob(): # Hapus parameter 'Kabupaten' dari sini
    # Panggil fungsi model untuk mendapatkan data sebagai list
    kabupaten_list = get_Kabupaten_data()
    daya_beli_list = get_Total_Daya_Beli_Masyarakat_data()

    # Pastikan kedua list berhasil diambil sebelum melanjutkan
    if kabupaten_list is None or daya_beli_list is None:
        st.warning("Data tidak dapat ditampilkan karena gagal diambil.")
        return # Hentikan eksekusi fungsi jika data tidak ada

    # Buat DataFrame langsung dari list yang sudah ada
    df = pd.DataFrame({
        "Kabupaten": kabupaten_list,
        "Daya Beli/ Kabupaten": daya_beli_list,
    })

    # Tambahkan label kategori dan warna
    df["Kategori"] = df["Daya Beli/ Kabupaten"].apply(get_color_label_dayaBelimob)
    warna_dict = {
        "Rendah": "#E30511", "Sedang": "#FD9B2A", "Tinggi": "#229122"
    }

    # Bar chart dengan warna dan legend
    bar = alt.Chart(df).mark_bar().encode(
        x=alt.X('Kabupaten:N', sort=None, title='Kabupaten'),
        y=alt.Y('Daya Beli/ Kabupaten:Q', title='Total Daya Beli Masyarakat'),
        color=alt.Color('Kategori:N',
                        scale=alt.Scale(domain=list(warna_dict.keys()), range=list(warna_dict.values())),
                        legend=alt.Legend(orient="top", title="Kategori Daya Beli")),
        tooltip=['Kabupaten', 'Daya Beli/ Kabupaten', 'Kategori']
    ).properties(height=550, width=900)

    text = alt.Chart(df).mark_text(
        align='center',
        baseline='bottom',
        dy=-5
    ).encode(
        x=alt.X('Kabupaten:N'),
        y=alt.Y('Daya Beli/ Kabupaten:Q'),
        tooltip=['Kabupaten', 'Daya Beli/ Kabupaten', 'Kategori'],
        text=alt.Text('Daya Beli/ Kabupaten:Q', format=",.0f")
    )

    st.altair_chart(bar + text, use_container_width=True) # Tampilkan chart (tanpa text agar tidak terlalu ramai)
