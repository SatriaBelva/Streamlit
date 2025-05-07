import streamlit as st
import pandas as pd
from controller import *
from model import *

col1, col2 = st.columns(2)
with col1 :
    graph_ListAktif_TotalHousehold()
with col2 :
    graph_PortAvail_TotalPort()

col1, col2 = st.columns(2)
with col1 :
    graph_WifiShare()
with col2 :
    graph_ODP()

tableADOIH()