import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from matplotlib import pyplot as plt

st.title("Charts Element")
st.text("Pada Page ini kita akan belajar mengenai cara membuat Grafik Data menggunakan Components yang ada di streamlit dengan sedikit bantuan dari library pandas dan numpy")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.subheader("Line Chart")
st.line_chart(chart_data, use_container_width=True, x_label='Random X Label', y_label='Random Y Label') 
st.divider()

st.subheader("Area Chart")
st.area_chart(chart_data, use_container_width=True, x_label='Random X Label', y_label='Random Y Label') 
st.divider()

st.subheader("Bar Chart")
st.bar_chart(chart_data, use_container_width=True, x_label='Random X Label', y_label='Random Y Label') 
st.divider()

st.subheader("Scatter Plot Chart")
scatter_data = pd.DataFrame({
    'x' : np.random.randn(100),
    'y' : np.random.randn(100),
})
st.scatter_chart(scatter_data, use_container_width=True, x_label='Random X Label', y_label='Random Y Label') 
st.divider()

