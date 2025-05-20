import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
from st_aggrid import AgGrid,  GridOptionsBuilder

def tableMarket() :
    data = pd.DataFrame(
        {   
            'Kabupaten'         : get_Kabupaten_data(),
            'FB Share REG'      : get_FacebookShare_data(),
            'Status REG'        : get_StatugReg_data(),
            'Close COMP REG'    : get_CloseCompetitionReg_data(),
            'FB Share Youth'    : get_FacebookShareYouth_data(),
            'Status Youth'      : get_StatusYouth_data(),
            'Close COMP Youth'  : get_CloseCompetitionYouth_data(),
        }
    )

    
    gb = GridOptionsBuilder.from_dataframe(data)
    # Define column groups
    gb.configure_column("Kabupaten", header_name="Kabupaten")
    gb.configure_column("FB Share REG", header_name="FB Share REG")
    gb.configure_column("Status REG", header_name="Status REG")
    gb.configure_column("Close COMP REG", header_name="Close COMP REG")
    gb.configure_column("FB Share Youth", header_name="FB Share Youth")
    gb.configure_column("Status Youth", header_name="Status Youth")
    gb.configure_column("Close COMP Youth", header_name="Close COMP Youth")
    gb.configure_grid_options(domLayout='autoHeight')
    gb.configure_default_column(resizable=True, minWidth=100, flex=2)
    gb.configure_default_column(flex=2)
    
    grid_options = gb.build()
    grid_options["columnDefs"] = [
        {"headerName": "Kabupaten", "field": "Kabupaten"},
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
        }
    }

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
        fit_columns_on_grid_load=True
    )



def refreshButton() :
    if st.button("Refresh Data", icon='🔁'):
        st.cache_data.clear()