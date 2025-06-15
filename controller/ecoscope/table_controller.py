import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode


def get_kategori_image_list():
    """
    Mengambil daftar URL gambar berdasarkan kategori ekonomi.
    Fungsi ini tetap sama karena sudah menghasilkan output yang dibutuhkan (URL).
    """
    kategori_list = get_kategori_ekonomi_data()["Kategori Ekonomi"].tolist()
    kategori_to_image = {
        "Tinggi": "https://github.com/SatriaBelva/TelekomunikasiSelular/blob/main/streamlit/assets/Badge-Tinggi-V3.png?raw=true",
        "Sedang": "https://github.com/SatriaBelva/TelekomunikasiSelular/blob/main/streamlit/assets/Badge-Sedang-V3.png?raw=true",
        "Rendah": "https://github.com/SatriaBelva/TelekomunikasiSelular/blob/main/streamlit/assets/Badge-Rendah-V3.png?raw=true",
    }
    return [kategori_to_image.get(kat, "") for kat in kategori_list]

def tableEcoscope(kecamatan):
    """
    Menampilkan tabel Ecoscope menggunakan AgGrid dengan gaya dari Populytics.
    Tabel ini akan menampilkan data per kecamatan atau per kelurahan berdasarkan pilihan.
    """
    # Renderer untuk menampilkan gambar dari URL menggunakan JsCode
    image_renderer = JsCode("""
        class ThumbnailRenderer {
            init(params) {
                this.eGui = document.createElement('img');
                if (params.value) {
                    this.eGui.setAttribute('src', params.value);
                    this.eGui.setAttribute('width', '100%');
                    this.eGui.setAttribute('height', '30');
                    this.eGui.style.objectFit = 'contain';
                }
            }
            getGui() {
                return this.eGui;
            }
        }
    """)

    # Custom CSS yang diadaptasi dari gaya Populytics
    custom_css = {
        ".ag-header-group-cell": {
            "background-color": "#D70000",
            "color": "white",
            "font-weight": "bold",
            "align-items": "center",
            "justify-content": "center",
            "text-align": "center"
        },
        ".ag-header-cell-comp-wrapper": {
            "align-items": "center",
            "justify-content": "center",
            "text-align": "center"
        },
        ".ag-header-cell-label": {
            "justify-content": "center",
            "display": "flex",
            "align-items": "center",
            "text-align": "center"
        },
        ".ag-header-cell": {
            "text-align": "center",
            "border-right": "1px solid #ccc",
            "border-bottom": "1px solid #ccc"
        },
        ".ag-cell": {
            "border-right": "1px solid #ccc",
            "border-bottom": "1px solid #ccc",
            "text-align": "center"
        },
        ".ag-row-even": {
            "background-color": "#EBEAE8"
        },
        ".ag-row-odd": {
            "background-color": "white"
        },
        ".ag-row:last-child": {
            "background-color": "#E40000",
            "color": "white",
            "font-weight": "bold"
        }
    }

    data = pd.DataFrame({   
        'Kecamatan' : get_kecamatan_data()["nama"].tolist(),
        'Jumlah Penduduk' : get_jumlah_penduduk_data(kecamatan)["Jumlah Penduduk"].tolist(),
        'Indeks Ekonomi' : get_indeks_ekonomi_table()["Indeks Ekonomi"].tolist(),
        'Kategori Ekonomi' : get_kategori_image_list(),
        'Pelajar Mahasiswa' : get_kategori_Pelajar_Mahasiswa()["Pelajar Mahasiswa"].tolist(),
        'IRT' : get_kategori_IRT()["IRT"].tolist(),
        'Nelayan Perdagangan Wiraswasta': get_kategori_Nelayan_Perdagangan_Wiraswasta()["Nelayan Perdagangan Wiraswasta"].tolist(),
        'Guru Perawat Pengacara' : get_kategori_Guru_Perawat_Pengacara()["Guru Perawat Pengacara"].tolist(),
        'Total Usia Produktif' : get_kategori_Total_Usia_Produktif()["Total Usia Produktif"].tolist(),
        'Daya Beli' : get_DayaBeli(kecamatan)["Daya Beli/ Kecamatan"].tolist(),
    })
    first_column_name = "Kecamatan"

    # Konfigurasi dasar AgGrid
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_column(first_column_name, headerName="Kecamatan")
    gb.configure_column("Kategori Ekonomi", headerName="Kategori", cellRenderer=image_renderer, width=150)
    
    # Konfigurasi untuk kolom numerik agar bisa diformat
    numeric_cols = ['Jumlah Penduduk', 'Indeks Ekonomi', 'Pelajar Mahasiswa', 'IRT',
                    'Nelayan Perdagangan Wiraswasta', 'Guru Perawat Pengacara',
                    'Total Usia Produktif', 'Daya Beli']
    for col in numeric_cols:
        gb.configure_column(col, type=["numericColumn", "numberColumnFilter", "customNumericFormat"], precision=0 if col != 'Indeks Ekonomi' else 2)
    
    grid_options = gb.build()

    # Mendefinisikan struktur header grup secara manual
    grid_options['columnDefs'] = [
        {"headerName": "Kecamatan", "field": first_column_name, "pinned": "left", "width": 150},
        {"headerName": "Jumlah Penduduk", "field": "Jumlah Penduduk"},
        {"headerName": "Indeks Ekonomi", "field": "Indeks Ekonomi"},
        {"headerName": "Kategori", "field": "Kategori Ekonomi", "cellRenderer": image_renderer, "width": 120},
        {
            "headerName": "Kategori usia Produktif",
            "children": [
                {"headerName": "Pelajar/Mhs", "field": "Pelajar Mahasiswa"},
                {"headerName": "IRT", "field": "IRT"},
                {"headerName": "Nelayan/Dagang/Wiraswasta", "field": "Nelayan Perdagangan Wiraswasta", "width": 250},
                {"headerName": "Guru/Perawat/Pengacara", "field": "Guru Perawat Pengacara", "width": 220},
            ]
        },
        {"headerName": "Total Usia Produktif", "field": "Total Usia Produktif"},
        {"headerName": "Daya Beli (Rp)", "field": "Daya Beli"},
    ]

    # Menambahkan baris total
    for kolom in numeric_cols:
        data[kolom] = pd.to_numeric(data[kolom], errors='coerce').fillna(0)

    if not data.empty:
        total_row = {first_column_name: 'Total', 'Kategori Ekonomi': ''}
        for kolom in numeric_cols:
            if kolom == 'Indeks Ekonomi':
                # Untuk Indeks Ekonomi, gunakan rata-rata
                mean_val = data[kolom][data[kolom] > 0].mean()
                total_row[kolom] = mean_val if not pd.isna(mean_val) else 0
            else:
                # Untuk kolom lain, gunakan jumlah
                total_row[kolom] = data[kolom].sum()
        
        data = pd.concat([data, pd.DataFrame([total_row])], ignore_index=True)

    # Menampilkan AgGrid
    return AgGrid(
        data,
        gridOptions=grid_options,
        custom_css=custom_css,
        theme="alpine",
        use_container_width=True,
        allow_unsafe_jscode=True,
        reload_data=True,
        fit_columns_on_grid_load=False, # Dinonaktifkan karena lebar kolom diatur manual
    )
