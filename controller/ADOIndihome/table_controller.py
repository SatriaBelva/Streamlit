import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *

def tableADOIH() :
    data = pd.DataFrame(
        {   
            'Kabupaten'         : get_Kabupaten_data(),
            'Total Household'   : get_TotalHousehold_data(),
            'LIS Aktif'         : get_ListAktif_data(),
            'WIFI SHARE'        : get_WifiShare_data(),
            'Close COMP'        : get_CloseComp_data(),
            'Total ODP'         : get_ODP_data(),
            'PORT Available'    : get_PortAvail_data(),
            'Total PORT'        : get_TotalPort_data(),
        }
    )
    return st.dataframe(data,use_container_width=True, hide_index=True)