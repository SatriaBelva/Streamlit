import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *

def tableEcoscope(kecamatan) :
    data = pd.DataFrame(
        {   
            'Nomor'              : get_kecamatan_data()["nama"].tolist(),
            'Kecamatan'          : get_kecamatan_data()["nama"].tolist(),
            'Jumlah Penduduk'    : get_jumlah_penduduk_data(kecamatan)["Jumlah Penduduk"].tolist(),
            'Indeks Ekonomi'     : get_indeks_ekonomi_table()["Indeks Ekonomi"].tolist(),
            'Kategori Ekonomi'   : get_kategori_image_list(),
        }
    )

    return st.data_editor(data,
        column_config={
                        "Kategori Ekonomi": st.column_config.ImageColumn(
                            "Kategori Ekonomi",
                            help="Tampilan badge ekonomi berdasarkan kategori",
                        )
                    },
        hide_index=True,
        use_container_width=True
    )

def get_kategori_image_list():
    kategori_list = get_kategori_ekonomi_data()["Kategori Ekonomi"].tolist()
    kategori_to_image = {
        "Tinggi": "https://github.com/SatriaBelva/TelekomunikasiSelular/blob/main/streamlit/assets/Badge-Tinggi-V3.png?raw=true",
        "Sedang": "https://github.com/SatriaBelva/TelekomunikasiSelular/blob/main/streamlit/assets/Badge-Sedang-V3.png?raw=true",
        "Rendah": "https://github.com/SatriaBelva/TelekomunikasiSelular/blob/main/streamlit/assets/Badge-Rendah-V3.png?raw=true",
    }
    return [kategori_to_image.get(kat, "") for kat in kategori_list]
     

