import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from matplotlib import pyplot as plt
from controller import *


st.title("Data Element")
st.text("Pada Page ini kita akan belajar mengenai cara membuat dashboard data menggunakan Components yang ada di streamlit dengan sedikit bantuan dari library pandas")

himasif = pd.DataFrame({
    'Kaderisasi' : ['Taqiyyah', 'Jeje', 'Shofia', 'Robbi', 'Juki', 'Nadhira', 'Nisa', 'Nabil', 'Edryan'],
    'Litbang'    : ['Bagus', 'Mada', 'Ica', 'Brilli', 'Rendy', 'Jasmin', 'Yesi', 'Jopay', None],
    'Humas'      : ['Ila', 'Rhenata', 'Hilmi', 'Raffy', 'Chelsea', 'Vivi', 'Muttaqin', None, None],
    'Mediatek'   : ['Muza', 'Jo', 'Dini', 'Rahardan', 'Tyo', 'Nabila', 'Almas', 'Rafi', 'Oktavia'],
    'PSDM'       : ['Eva', 'Dewi', 'Nathan', 'Felix', 'Ziza', 'Viola', 'Derrick', 'Iklina', 'Kanina']
})

st.subheader("Menggunakan Write")
st.write(himasif)
st.caption("Apabila menggunakan write maka dashboardnya akan memiliki fungsionalitas seperti sorting Column")
st.divider()

st.subheader("Menggunakan dataframe")
st.dataframe(himasif)
st.caption("Apabila menggunakan dataframe maka dashboardnya akan memiliki fungsionalitas seperti sorting Column")
st.divider()

st.subheader("Menggunakan data_editor")
st.data_editor(himasif)
st.caption('''Apabila menggunakan data_editor maka dashboardnya akan memiliki fungsionalitas seperti sorting Column + **Bisa Diedit Datanya**''')
st.divider()

st.table(himasif)
st.caption("Apabila menggunakan table maka dashboardnya akan statis menampilkan datanya saja")


st.subheader("Menampilkan Metric")
st.metric(label="Jumlah Divisi", value=f'Jumlah Divisi di HIMASIF ada {len(himasif.columns)}', delta=-1, delta_color='normal', border=True)
st.metric(label="Suhu Ruangan Sekretarian HIMASIF", value="20ᴼ Celcius", delta='-5ᴼ Celcius', delta_color='inverse', border=True)
st.metric(label="Jumlah Uang Kas HIMASIF 2024/2025", value=f'Rp2.000.000', delta='Rp500.000', delta_color='normal', border=False, label_visibility='visible', help='Metric Ini berisi informasi mengenai Jumlah uang kas HIMASIF periode 2024/2025 beserta selisihnya dari bulan lalu') 
st.divider()

st.subheader("Menampilkan Data Json")
json = {
    "nama" : ['Satria Belva Nararya', 'Safila Elsa Vavilya', 'Felisita Dian Puspitasari'],
    'umur' : [22, 20, 20],
    'asal divisi' : ['Kaderisasi', 'Litbang', 'Humas']
}

st.json(json)
st.divider()

# akunData()
