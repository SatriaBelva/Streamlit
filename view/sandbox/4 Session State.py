import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from matplotlib import pyplot as plt
from utils import clearTerminal, testingCheckbox, pilihanDivisi, organizationSelection, previewUploadedFile, usernameAndPassword, registration

st.title("Session State")
st.text("Pada Page ini kita akan belajar mengenai cara menggunakan session state")

st.code('st.session_state')
st.caption('st.session_state di Streamlit itu adalah tempat untuk menyimpan data sementara selama aplikasi Streamlit kamu berjalan.')
st.markdown(''' Kapan st.session_state Berguna?\n
✅ Menyimpan data form sementara

✅ Menyimpan status login user

✅ Tracking step di multi-page app

✅ Menyimpan hasil query dari database biar gak query ulang tiap rerun

✅ Menyimpan pilihan user di dropdown, checkbox, radio, dsb.
''')

st.markdown('Session State Hampir sama konsepnya dengan dictionary di python yaitu dia memiliki pasangan key dan value')
st.code('''
# Menyimpan data ke session_state
st.session_state['nama']   = 'Satria Belva Nararya'
st.session_state.gender    = 'Laki Laki'
st.session_state.umur      = 20

# Looping untuk menampilkan semua key dan value
for key, value in st.session_state.items():
    st.write(f"{key} = {value}")
''', language='python')

st.divider()
st.header('Contoh Penerapan Session State')

if 'counter' not in st.session_state :
      st.session_state.counter = 0
if st.button(label='Increment Counter') :
      st.session_state.counter += 1
      st.metric(label="Berapa Kali Button Diklik?", value=f'Counter : {st.session_state.counter}', delta=f'{st.session_state.counter}', delta_color='normal', help='Metric Ini berisi informasi mengenai berapa kali button diklik') 
if st.button(label='Reset Counter to 0'):
     st.session_state.counter = 0


st.divider()
