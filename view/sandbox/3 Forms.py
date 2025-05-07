import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from matplotlib import pyplot as plt
from utils import clearTerminal, testingCheckbox, pilihanDivisi, organizationSelection, previewUploadedFile, usernameAndPassword, registration

st.title("Forms Element")
st.text("Pada Page ini kita akan belajar mengenai cara membuat dashboard data menggunakan Components yang ada di streamlit dengan sedikit bantuan dari library pandas")

# Contoh 1
st.markdown("<h1 style='text-align : center;'>User Registration</h1>", unsafe_allow_html=True)
with st.form(key='form2', clear_on_submit=False, enter_to_submit=False) : # Harus menggunakan with agar aplikasi tidak rerun setiap ada perubahan di widgetnya dan hanya direrun setelah form disubmit melalui submit button     
    col1, col2, col3 = st.columns(spec=3)
    firstname    = col1.text_input(label='Firstname')
    surname      = col2.text_input(label='Surname')
    lastname     = col3.text_input(label='Lastname')
    username     = st.text_input(label='Username', help='username harus unik')
    birthdate    = st.date_input(label='Silahkan Pilih Tanggal Lahir Anda',help='Silahkan Pilih Tanggal Lahir Anda',format='DD/MM/YYYY',max_value=datetime.date.today(),min_value=datetime.date(1925, 6, 23), value=datetime.date(2002, 8, 31) )
    password1    = st.text_input(label='Password', type='password', help='password boleh berbeda')
    password2    = st.text_input(label='Confirm Password', type='password')
    submitButton = st.form_submit_button(label='Submit', use_container_width=True, type='secondary', on_click=registration )
    if submitButton :
        if firstname == "" or surname == "" or lastname == "" :
            st.warning(body="Please Fill in Your Name", icon='⚠️')
        elif username == "" :
            st.error(body="Goblog", icon='🧠')
        elif password1 == "":
            st.warning(body="Password Tidak Boleh Kosong", icon='⚠️')
        elif password2 == "":
            st.warning(body="Tolong Konfirmasi Password Anda", icon='⚠️')
        elif password1 != password2 :
            st.warning(body="Password Tidak Sama", icon='⚠️')
        else : 
            # Simpan ke session_state sebelum memanggil fungsi
            st.session_state['registration'] = {
                "firstname": firstname,
                "surname": surname,
                "lastname": lastname,
                "username": username,
                "birthdate": birthdate,
                "password": password1
            }
            st.success(body="Akun Berhasil Dibuat!", icon='🔥')
            registration()

# Contoh 2
form_values = {
    "Nama" : None,
    "Divisi" : None,
    "Periode" : None,
    "Jenis Kelamin" : None
}

with st.form(key='form1', clear_on_submit=False, enter_to_submit=False) :
    col1, col2, col3 = st.columns(spec=3)
    form_values['Nama']          = col1.text_input(label='Nama')
    form_values['Divisi']        = col2.selectbox(label='Divisi', options=['Choose an option', 'Humas', 'Kaderisasi', 'Litbang', 'Mediatek', 'PSDM'])
    form_values['Periode']       = col3.selectbox(label='Periode', options=['Choose an option', 2022, 2023, 2024])
    form_values['Jenis Kelamin'] = st.selectbox(label='Jenis Kelamin', options=['Choose an option', 'Laki-Laki', 'Perempuan'])

    submitButton = st.form_submit_button(label='Submit', use_container_width=True, type='secondary')
    if submitButton :
        if not all(form_values.values()) :
            st.error(body="Please Fill all of the fields", icon='⚠️')
        elif form_values['Divisi'] == 'Choose an option' :
            st.warning(body="Silahkan Pilih Divisi", icon='😡')
        elif form_values['Periode'] == 'Choose an option' :
            st.warning(body="Silahkan Pilih Periode Kamu", icon='😡')
        elif form_values['Jenis Kelamin'] == 'Choose an option' :
            st.warning(body="Silahkan Pilih Jenis Kelamin Kamu", icon='😡')
        else :
            st.balloons()    
            st.write("### Anngota Info")
            for (key,values) in form_values.items() :
                st.write(f'{key} : {values}')

                                         