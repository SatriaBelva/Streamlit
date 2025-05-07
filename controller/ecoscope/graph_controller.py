import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *

def graphIndeksEkonomi(kecamatan):
    if kecamatan == "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                "Kecamatan"          : get_kecamatan_data()["nama"].tolist(),
                "Indeks Ekonomi"     : get_indeks_ekonomi(kecamatan)["Indeks Ekonomi"].tolist(),
            }
        )
        st.bar_chart(dataPendidikan, x="Kecamatan", y="Indeks Ekonomi", horizontal=False, stack=True, color="#E30511", height=550)
    elif kecamatan != "Semua" : 
        dataPendidikan = pd.DataFrame(
            {
                "Kecamatan"    : get_kecamatan_data()["nama"].tolist(),
                "Indeks Ekonomi"                            : get_indeks_ekonomi(kecamatan)["Indeks Ekonomi"].tolist()
            }
        )
        st.bar_chart(dataPendidikan, x="Kecamatan", y="Indeks Ekonomi", horizontal=False, stack=True, color="#E30511", height=550)

