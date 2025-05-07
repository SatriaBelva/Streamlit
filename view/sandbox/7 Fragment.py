import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from matplotlib import pyplot as plt

st.title("Charts Element")
st.text("Pada Page ini kita akan belajar mengenai cara membuat Grafik Data menggunakan Components yang ada di streamlit dengan sedikit bantuan dari library pandas dan numpy")


if st.button("Check click count"):
    st.toast(f"## Total clicks:")