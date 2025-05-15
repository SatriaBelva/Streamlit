import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
import altair as alt

# dataKecamatan = kecamatan_list()

def graphPendidikan(kecamatan):
    if kecamatan == "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                "Kecamatan"                                     : get_kecamatan_data()["nama"].tolist(),
                "Tidak/putus sekolah, belum tamat SD, tamat SD" : get_belum_sekolah_data(kecamatan)["Tidak/putus sekolah, belum tamat SD, tamat SD"].tolist(),
                "SLTP/SLTA"                                     : get_SLTPSLTA_data(kecamatan)["SLTP/SLTA"].tolist(),
                "D1/D2, D3, S1, S2, S3"                         : get_kuliah_data(kecamatan)["kuliah"].tolist()
            }
        )
        st.bar_chart(dataPendidikan, x="Kecamatan", y=["Tidak/putus sekolah, belum tamat SD, tamat SD", "SLTP/SLTA", "D1/D2, D3, S1, S2, S3"], horizontal=False, stack=True, color=["#229122", "#FD9B2A", "#E30511"], height=550)
    elif kecamatan != "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                f"Kelurahan di {kecamatan.capitalize()}"        : get_kelurahan_data(kecamatan)["nama"].tolist(),
                "Tidak/putus sekolah, belum tamat SD, tamat SD" : get_belum_sekolah_data(kecamatan)["Tidak/putus sekolah, belum tamat SD, tamat SD"].tolist(),
                "SLTP/SLTA"                                     : get_SLTPSLTA_data(kecamatan)["SLTP/SLTA"].tolist(),
                "D1/D2, D3, S1, S2, S3"                         : get_kuliah_data(kecamatan)["kuliah"].tolist()
            }
        )
        st.bar_chart(dataPendidikan, x=f"Kelurahan di {kecamatan.capitalize()}", y=["Tidak/putus sekolah, belum tamat SD, tamat SD", "SLTP/SLTA", "D1/D2, D3, S1, S2, S3"], horizontal=False, stack=True, color=["#229122", "#FD9B2A", "#E30511"], height=550)

def graphPekerjaan(kecamatan):
    if kecamatan == "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                "Kecamatan"                                              : get_kecamatan_data()["nama"].tolist(),
                "Tidak/Belum Bekerja, Pelajar/Mahasiswa, IRT, Pensiunan" : get_firstCategory_data(kecamatan)["Category 1"].tolist(),
                "Perdagangan, Wiraswasta, Nelayan"                       : get_secondCategory_data(kecamatan)["Category 2"].tolist(),
                "Guru, Perawat, Pengacara"                               : get_ThirdCategory_data(kecamatan)["Category 3"].tolist()
            }
        )
        st.bar_chart(dataPendidikan, x="Kecamatan", y=["Tidak/Belum Bekerja, Pelajar/Mahasiswa, IRT, Pensiunan", "Perdagangan, Wiraswasta, Nelayan", "Guru, Perawat, Pengacara"], horizontal=False, stack=True, color=["#229122", "#FD9B2A", "#E30511"], height=550)
    elif kecamatan != "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                f"Kelurahan di {kecamatan.capitalize()}"                 : get_kelurahan_data(kecamatan)["nama"].tolist(),
                "Tidak/Belum Bekerja, Pelajar/Mahasiswa, IRT, Pensiunan" : get_firstCategory_data(kecamatan)["Category 1"].tolist(),
                "Perdagangan, Wiraswasta, Nelayan"                       : get_secondCategory_data(kecamatan)["Category 2"].tolist(),
                "Guru, Perawat, Pengacara"                               : get_ThirdCategory_data(kecamatan)["Category 3"].tolist()
            }
        )
        st.bar_chart(dataPendidikan, x=f"Kelurahan di {kecamatan.capitalize()}", y=["Tidak/Belum Bekerja, Pelajar/Mahasiswa, IRT, Pensiunan", "Perdagangan, Wiraswasta, Nelayan", "Guru, Perawat, Pengacara"], horizontal=False, stack=True, color=["#229122", "#FD9B2A", "#E30511"], height=550)

# def graphJumlahPenduduk(kecamatan):
#     if kecamatan == "Semua" : 
#         dataPendidikan = pd.DataFrame(
#             {
#                 "Kecamatan" : get_kecamatan_data()["nama"].tolist(),
#                 "Jumlah Penduduk" : get_jumlah_penduduk_data(kecamatan)["Jumlah Penduduk"].tolist(),
#             }
#         )
#         return st.bar_chart(dataPendidikan, x="Kecamatan", y="Jumlah Penduduk", horizontal=False, stack=True, color="#E30511", height=550)
#     elif kecamatan != "Semua" : 
#         dataPendidikan = pd.DataFrame(
#             {
#                 f"Kelurahan di {kecamatan.capitalize()}"    : get_kelurahan_data(kecamatan)["nama"].tolist(),
#                 "Jumlah Penduduk"                           : get_jumlah_penduduk_popultycs_data(kecamatan)["Jumlah Penduduk"].tolist()
#             }
#         )
#         return st.bar_chart(dataPendidikan, x=f"Kelurahan di {kecamatan.capitalize()}", y="Jumlah Penduduk", horizontal=False, stack=True, color="#E30511", height=550)
def graphJumlahPenduduk(kecamatan):
    if kecamatan == "Semua":
        df = pd.DataFrame({
            "Kecamatan"         : get_kecamatan_data()["nama"].tolist(),
            "Jumlah Penduduk"   : get_jumlah_penduduk_data(kecamatan)["Jumlah Penduduk"].tolist(),
        })

        chart = alt.Chart(df).mark_bar(color="#E30511").encode(
            x=alt.X("Kecamatan:N"),  # tanpa sort
            y="Jumlah Penduduk:Q"
        ).properties(height=550)

        text = alt.Chart(df).mark_text(
            align="center", baseline="bottom", dy=-5
        ).encode(
            x=alt.X("Kecamatan:N"),
            y="Jumlah Penduduk:Q",
            text=alt.Text("Jumlah Penduduk:Q", format=",")  # format angka ribuan
        )

        st.altair_chart(chart + text, use_container_width=True)

    else:
        kel_label = f"Kelurahan di {kecamatan.capitalize()}"
        df = pd.DataFrame({
            kel_label           : get_kelurahan_data(kecamatan)["nama"].tolist(),
            "Jumlah Penduduk"   : get_jumlah_penduduk_popultycs_data(kecamatan)["Jumlah Penduduk"].tolist(),
        })

        chart = alt.Chart(df).mark_bar(color="#E30511").encode(
            x=alt.X(f"{kel_label}:N"),  # tanpa sort
            y="Jumlah Penduduk:Q"
        ).properties(height=550)

        text = alt.Chart(df).mark_text(
            align="center", baseline="bottom", dy=-5
        ).encode(
            x=alt.X(f"{kel_label}:N"),
            y="Jumlah Penduduk:Q",
            text=alt.Text("Jumlah Penduduk:Q", format=",")
        )

        st.altair_chart(chart + text, use_container_width=True)
        

# def graphJumlahKK(kecamatan):
#     if kecamatan == "Semua" : 
#         dataPendidikan = pd.DataFrame(
#             {
#                 "Kecamatan"                 : get_kecamatan_data()["nama"].tolist(),
#                 "Jumlah Kartu Keluarga"     : get_jumlahKK_data(kecamatan)["Jumlah Kartu Keluarga"].tolist(),
#             }
#         )
#         st.bar_chart(dataPendidikan, x="Kecamatan", y="Jumlah Kartu Keluarga", horizontal=False, stack=True, color="#E30511", height=550)
#     elif kecamatan != "Semua" : 
#         dataPendidikan = pd.DataFrame(
#             {
#                 f"Kelurahan di {kecamatan.capitalize()}"    : get_kelurahan_data(kecamatan)["nama"].tolist(),
#                 "Jumlah Kartu Keluarga"                     : get_jumlahKK_data(kecamatan)["Jumlah Kartu Keluarga"].tolist()
#             }
#         )
#         st.bar_chart(dataPendidikan, x=f"Kelurahan di {kecamatan.capitalize()}", y="Jumlah Kartu Keluarga", horizontal=False, stack=True, color="#E30511", height=550)

def graphJumlahKK(kecamatan):
    if kecamatan == "Semua" : 
        df = pd.DataFrame(
            {
                "Kecamatan"                 : get_kecamatan_data()["nama"].tolist(),
                "Jumlah Kartu Keluarga"     : get_jumlahKK_data(kecamatan)["Jumlah Kartu Keluarga"].tolist(),
            }
        )
        chart = alt.Chart(df).mark_bar(color="#E30511").encode(
            x=alt.X("Kecamatan:N"),  # tanpa sort
            y="Jumlah Kartu Keluarga:Q"
        ).properties(height=550)

        text = alt.Chart(df).mark_text(
            align="center", baseline="bottom", dy=-5
        ).encode(
            x=alt.X("Kecamatan:N"),
            y="Jumlah Kartu Keluarga:Q",
            text=alt.Text("Jumlah Kartu Keluarga:Q", format=",")  # format angka ribuan
        )

        st.altair_chart(chart + text, use_container_width=True)
    else:
        kel_label = f"Kelurahan di {kecamatan.capitalize()}"
        df = pd.DataFrame({
            kel_label: get_kelurahan_data(kecamatan)["nama"].tolist(),
            "Jumlah Kartu Keluarga": get_jumlahKK_data(kecamatan)["Jumlah Kartu Keluarga"].tolist(),
        })

        chart = alt.Chart(df).mark_bar(color="#E30511").encode(
            x=alt.X(f"{kel_label}:N"),
            y=alt.Y("Jumlah Kartu Keluarga:Q")
        ).properties(height=550)

        text = alt.Chart(df).mark_text(
            align="center", baseline="bottom", dy=-5
        ).encode(
            x=alt.X(f"{kel_label}:N"),
            y="Jumlah Kartu Keluarga:Q",
            text=alt.Text("Jumlah Kartu Keluarga:Q", format=",")
        )

        st.altair_chart(chart + text, use_container_width=True)