import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *

def table() :
    data = pd.DataFrame(
        {   
            'Kabupaten'         : get_Kabupaten_data(),
            'Populasi'          : get_Populasi_data(),
            'ARPU'              : get_Populasi_data(),
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
        }
    )
    st.dataframe(data,use_container_width=True, hide_index=True)

def refreshButton() :
    if st.button("Refresh Data", icon='🔁'):
        st.cache_data.clear()