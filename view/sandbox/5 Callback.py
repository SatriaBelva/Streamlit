import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from matplotlib import pyplot as plt

st.title("Callback")
st.text("Pada Page ini kita akan belajar mengenai cara membuat dashboard data menggunakan Components yang ada di streamlit dengan sedikit bantuan dari library pandas")
st.write('Callback akan dijalankan pertama kali ketika rerun')

st.code('''
    # Fungsi callback yang akan dipanggil saat tombol diklik
    def simpan_biodata():
        st.session_state["biodata_disimpan"] = True

    # Form dengan input nama dan umur
    with st.form("form_biodata"):
        nama = st.text_input("Nama")
        umur = st.number_input("Umur", min_value=0, step=1)
        
        # Submit form akan memicu callback
        submitted = st.form_submit_button("Submit", on_click=simpan_biodata)

    # Tampilkan hasil jika biodata sudah disimpan
    if st.session_state.get("biodata_disimpan"):
        st.success("✅ Data berhasil disimpan!")
        st.write("📋 Biodata kamu:")
        st.write(f"Nama: {nama}")
        st.write(f"Umur: {umur}")
''')

if 'step' not in st.session_state :
    st.session_state['step'] = 1
if 'info' not in st.session_state :
    st.session_state.info = {}

def go_to_step_2(name) :
    st.session_state['step'] = 2
    st.session_state.info['name'] = name

def go_to_step_1():
    st.session_state['step'] = 1

if st.session_state.step == 1 :
    st.header("Step 1")
    name = st.text_input('Name', value=st.session_state.get("name", ""))  
    st.button('Go to Step 2', on_click=go_to_step_2,  args=(name,))

if st.session_state.step == 2 :
    st.header("Step 2")
    st.subheader("Please Review This Information")
    st.write(f'**Name** : {st.session_state.info.get('name','')}')
    if st.button(label='Submit', type='secondary') :
        st.success(f"Selamat Anda Adalah {st.session_state.info['name']}", icon="🔥")
        st.balloons()
    st.button(label='Back', type='primary', on_click=go_to_step_1)
        