import streamlit as st
import pandas as pd
from controller import *
from model import *

col1, col2 = st.columns(2)
with col1 :
    graphCB_Populasi()
with col2 :
    graph_FBREG_FBYouth()

col3, col2 = st.columns(2)
with col3 :
    # graph_ARPU()
    graph_Arpu()
with col2 :
    graph_OUTLETPJP()

graph_Site()

table()

refreshButton()