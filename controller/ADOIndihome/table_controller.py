import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
from st_aggrid import AgGrid,  GridOptionsBuilder

def tableADOIH() :
    data = pd.DataFrame(
        {   
            'Kabupaten'         : get_Kabupaten_data(),
            'Total Household'   : get_TotalHousehold_data(),
            'LIS Aktif'         : get_ListAktif_data(),
            'Penetration Rate'  : get_PENETRATION_RATE(),
            'WIFI SHARE'        : get_WifiShare_data(),
            'Close COMP'        : get_CloseComp_data(),
            'Total ODP'         : get_ODP_data(),
            'PORT Available'    : get_PortAvail_data(),
            'Total PORT'        : get_TotalPort_data(),
            'Port Share'        :get_PORT_SHARE(),
        }
    )
    

    # Custom CSS styles
    custom_css = {
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
        'Total Household', 'LIS Aktif', 'Total ODP', 'PORT Available',
        'Total PORT'
    ]

    for kolom in numerik_kolom:
        data[kolom] = pd.to_numeric(data[kolom], errors='coerce')
    total_row = {
        'Kabupaten': 'Total'
    }
    for kolom in numerik_kolom:
        total_row[kolom] = data[kolom].sum()

    gb = GridOptionsBuilder.from_dataframe(data)

    # 2. Konfigurasi kolom default agar fleksibel dan mengisi ruang
    #    Properti 'flex: 1' adalah kunci agar kolom memenuhi lebar grid.
    gb.configure_default_column(
        resizable=True,
        filterable=True,
        sortable=True,
        editable=False,
    )
    gridOptions = gb.build()
    # Tambahkan baris total
    data = pd.concat([data, pd.DataFrame([total_row])], ignore_index=True)
    AgGrid(
        data,
        gridOptions=gridOptions,  # Gunakan gridOptions yang sudah dibuat
        custom_css=custom_css,
        use_container_width=True, # Tetap diperlukan untuk memberitahu Streamlit agar mengizinkan lebar penuh
        theme="alpine",
        allow_unsafe_jscode=True,
        enable_enterprise_modules=True,
        reload_data=True
    )