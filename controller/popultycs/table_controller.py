import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *
from st_aggrid import AgGrid,  GridOptionsBuilder

def tablePopultycs(kecamatan) :
    if kecamatan == "Semua" :
        
        data = pd.DataFrame(
            {   
                'Kecamatan'                      : get_kecamatan_data()["nama"].tolist(),
                'Sekolah Tinggi'                 : get_kuliah_data(kecamatan)["kuliah"].tolist(),
                'Sekolah Menengah'               : get_SLTPSLTA_data(kecamatan)["SLTP/SLTA"].tolist(),
                'Tidak/Belum Sekolah & Tamat SD' : get_belum_sekolah_data(kecamatan)["Tidak/putus sekolah, belum tamat SD, tamat SD"].tolist(),
                'Tidak/Belum Bekerja'            : get_firstCategory_data(kecamatan)["Category 1"].tolist(),
                'Penghasilan Stabil'             : get_ThirdCategory_data(kecamatan)["Category 3"].tolist(),
                'Penghasilan Tidak Stabil'       : get_secondCategory_data(kecamatan)["Category 2"].tolist(),
                'Jumlah Penduduk'                : get_jumlah_penduduk_data(kecamatan)["Jumlah Penduduk"].tolist(),
                'Jumlah KK'                      : get_jumlahKK_data(kecamatan)["Jumlah Kartu Keluarga"].tolist(),
            }
        )
        # Custom CSS styles
        custom_css = {
            ".ag-header-group-cell": {
                "background-color": "#D70000",
                "color": "white",
                "font-weight": "bold",
            },
            ".ag-row-even": {
                "background-color": "#f5f5f5"
            },
            ".ag-row-odd": {
                "background-color": "white"
            },
            ".ag-cell": {
                "border-right": "1px solid #ccc",
                "border-bottom": "1px solid #ccc",
            },
            ".ag-header-cell": {
                "border-right": "1px solid #ccc",
                "border-bottom": "1px solid #ccc",
            },
        }

        AgGrid(
            data,
            custom_css=custom_css,
            use_container_width=True,
            theme="alpine",
            allow_unsafe_jscode=True,
            enable_enterprise_modules=True,
            reload_data=True,
            hide_index=True,
            autosize_all_columns=True,
        )
    elif kecamatan != "Semua" :
        data = pd.DataFrame(
            {   
                f"Kelurahan di {kecamatan.capitalize()}"    : get_kelurahan_data(kecamatan)["nama"].tolist(),
                'Sekolah Tinggi'                            : get_kuliah_data(kecamatan)["kuliah"].tolist(),
                'Sekolah Menengah'                          : get_SLTPSLTA_data(kecamatan)["SLTP/SLTA"].tolist(),
                'Tidak/Belum Sekolah & Tamat SD'            : get_belum_sekolah_data(kecamatan)["Tidak/putus sekolah, belum tamat SD, tamat SD"].tolist(),
                'Tidak/Belum Bekerja'                       : get_firstCategory_data(kecamatan)["Category 1"].tolist(),
                'Penghasilan Stabil'                        : get_ThirdCategory_data(kecamatan)["Category 3"].tolist(),
                'Penghasilan Tidak Stabil'                  : get_secondCategory_data(kecamatan)["Category 2"].tolist(),
                'Jumlah Penduduk'                           : get_jumlah_penduduk_popultycs_data(kecamatan)["Jumlah Penduduk"].tolist(),
                'Jumlah KK'                                 : get_jumlahKK_data(kecamatan)["Jumlah Kartu Keluarga"].tolist(),
            }
        )
        # Custom CSS styles
        custom_css = {
            ".ag-header-group-cell": {
                "background-color": "#D70000",
                "color": "white",
                "font-weight": "bold",
            },
            ".ag-row-even": {
                "background-color": "#f5f5f5"
            },
            ".ag-row-odd": {
                "background-color": "white"
            },
            ".ag-cell": {
                "border-right": "1px solid #ccc",
                "border-bottom": "1px solid #ccc",
            },
            ".ag-header-cell": {
                "border-right": "1px solid #ccc",
                "border-bottom": "1px solid #ccc",
            },
        }

        AgGrid(
            data,
            custom_css=custom_css,
            use_container_width=True,
            theme="alpine",
            autosize_all_columns=True,
            allow_unsafe_jscode=True,
            enable_enterprise_modules=True,
            reload_data=True,
            hide_index=True,

        )
# def table2() :
#     data = pd.DataFrame(
#         {   
#             'Kecamatan'     : dataKecamatan,
#             'Penduduk'      : np.random.randint(5000, 25000, size=len(dataKecamatan)),
#             'KartuKeluarga' : np.random.randint(5000, 25000, size=len(dataKecamatan)),
#         }
#     )

#     rows_per_page = 10
#     total_pages = len(data) // rows_per_page + (1 if len(data) % rows_per_page > 0 else 0)

#     if 'page' not in st.session_state:
#         st.session_state.page = 1

#     start_idx = (st.session_state.page - 1) * rows_per_page
#     end_idx = start_idx + rows_per_page
#     current_data = data.iloc[start_idx:end_idx]

#     st.dataframe(current_data, use_container_width=True, hide_index=True)

#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         pass
#     with col2:
#         if st.button("⬅️ Prev", key="prev_button", use_container_width=True, ) and st.session_state.page > 1:
#             st.session_state.page -= 1
#             st.rerun()
#     with col3:
#         st.markdown(
#             f"<div style='text-align: center; font-weight: normal; padding-top:6px;'>Page {st.session_state.page} of {total_pages}</div>",
#             unsafe_allow_html=True
#         )   
#     with col4:
#         if st.button("Next ➡️", key="next_button", use_container_width=True) and st.session_state.page < total_pages:
#             st.session_state.page += 1
#             st.rerun()
#     with col5:
#         pass