import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
from st_aggrid import AgGrid,  GridOptionsBuilder

def tableMobile() :
    data = pd.DataFrame(
        {   
            'Kabupaten'         : get_Kabupaten_data(),
            'Populasi'          : get_Populasi_data(),
            'ARPU'              : get_ARPU_data(),
            'CB'                : get_CB_data(),
            'Penetrasi CB'      : get_PenetrasiCB_data(),
            'Outlet PJP'        : get_OutletPJP_data(),
            'Site'              : get_Site_data(),
            'Coverage Share'    : get_CoverageShare_data(),
            'FB Share REG'      : get_FacebookShare_data(),
            'Status REG'        : get_StatugReg_data(),
            'Close COMP REG'    : get_CloseCompetitionReg_data(),
            'FB Share Youth'    : get_FacebookShareYouth_data(),
            'Status Youth'      : get_StatusYouth_data(),
            'Close COMP Youth'  : get_CloseCompetitionYouth_data(),
            'Pelajar Mahasiswa' : get_PelajarMahasiswa_data(),
            'IRT'                : get_IRT_data(),
            'Nelayan, Perdagangan, Wiraswasta' : get_Nelayan_Perdagangan_Wiraswasta_data(),
            'Total Usia Produktif' : get_Total_Usia_Produktif_data(),
            'Total Daya Beli Masyarakat' : get_Total_Daya_Beli_Masyarakat_data(),
        }
    )

    
    gb = GridOptionsBuilder.from_dataframe(data)
    # Define column groups
    gb.configure_column("FB Share REG", header_name="FB Share REG")
    gb.configure_column("Status REG", header_name="Status REG")
    gb.configure_column("Close COMP REG", header_name="Close COMP REG")
    gb.configure_column("FB Share Youth", header_name="FB Share Youth")
    gb.configure_column("Status Youth", header_name="Status Youth")
    gb.configure_column("Close COMP Youth", header_name="Close COMP Youth")

    grid_options = gb.build()

    grid_options["columnDefs"] = [
        {"headerName": "Kabupaten", "field": "Kabupaten"},
        {"headerName": "Populasi", "field": "Populasi"},
        {"headerName": "ARPU", "field": "ARPU"},
        {"headerName": "CB", "field": "CB"},
        {"headerName": "Penetrasi CB", "field": "Penetrasi CB"},
        {"headerName": "Outlet PJP", "field": "Outlet PJP"},
        {"headerName": "Site", "field": "Site"},
        {"headerName": "Coverage Share", "field": "Coverage Share"},
        {
            "headerName": "Regional",
            "headerClass": "red-header",
            "children": [
                {"headerName": "FB Share REG", "field": "FB Share REG"},
                {"headerName": "Status REG", "field": "Status REG"},
                {"headerName": "Close COMP REG", "field": "Close COMP REG"},
            ]
        },
        {
            "headerName": "Youth",
            "headerClass": "red-header",
            "children": [
                {"headerName": "FB Share Youth", "field": "FB Share Youth"},
                {"headerName": "Status Youth", "field": "Status Youth"},
                {"headerName": "Close COMP Youth", "field": "Close COMP Youth"},
            ]
        },
        {
            "headerName": "Kategori Usia Produktif",
            "headerClass": "red-header",
            "children": [
                {"headerName": "Pelajar Mahasiswa", "field": "Pelajar Mahasiswa"},
                {"headerName": "IRT", "field": "IRT"},
                {"headerName": "Nelayan, Perdagangan, Wiraswasta", "field": "Nelayan, Perdagangan, Wiraswasta"},
            ]
        },
        {"headerName": "Total Usia Produktif", "field": "Total Usia Produktif"},
        {"headerName": "Total Daya Beli Masyarakat", "field": "Total Daya Beli Masyarakat"},
    ]

    # Custom CSS styles
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
    numerik_kolom = [
        'Populasi', 'ARPU', 'CB',
        'Outlet PJP', 'Site',
        'FB Share REG',
        'FB Share Youth',
        'Pelajar Mahasiswa',
        'IRT',
        'Nelayan, Perdagangan, Wiraswasta',
        'Total Usia Produktif',
        'Total Daya Beli Masyarakat'
    ]
    kolom_desimal_koma = ['FB Share REG', 'FB Share Youth']

    for kolom in numerik_kolom:
        data[kolom] = data[kolom].astype(str).str.strip()

        if kolom not in kolom_desimal_koma:
            # Hapus titik ribuan
            data[kolom] = data[kolom].str.replace('.', '', regex=False)
            # Ubah koma ke titik (untuk desimal jika ada)
            data[kolom] = data[kolom].str.replace(',', '.', regex=False)
        else:
            # Untuk 'FB Share REG' & 'FB Share Youth': biarkan koma tetap sebagai desimal
            data[kolom] = data[kolom].str.replace('.', '', regex=False)  # hapus ribuan
            data[kolom] = data[kolom].str.replace(',', '.', regex=False)
            # Tapi JANGAN ubah koma ke titik

        data[kolom] = pd.to_numeric(data[kolom], errors='coerce')

    total_row = {
        'Kabupaten': 'Total'
    }
    for kolom in numerik_kolom:
        total_row[kolom] = data[kolom].sum()

    # Tambahkan baris total
    data = pd.concat([data, pd.DataFrame([total_row])], ignore_index=True)
    AgGrid(
        data,
        gridOptions=grid_options,
        custom_css=custom_css,
        use_container_width=True,
        theme="alpine",
        allow_unsafe_jscode=True,
        enable_enterprise_modules=True,
        reload_data=True,
        hide_index=True,
        autosize_all_columns=True,
    )



def refreshButton() :
    if st.button("Refresh Data", icon='🔁'):
        st.cache_data.clear()