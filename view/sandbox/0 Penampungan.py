import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from matplotlib import pyplot as plt
from utils import clearTerminal, testingCheckbox, pilihanDivisi, organizationSelection, previewUploadedFile, usernameAndPassword, registration

st.text("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eveniet aperiam explicabo quae veritatis sequi illum voluptates adipisci eius vel maxime laudantium cumque molestias odio, obcaecati aut rerum. Quos, at reiciendis.")
st.write(os.path.join(os.getcwd(), "Anjay", "Testing.pdf"))

st.markdown("1. **Satria Belva Nararya** -> [@satriabelva](https://www.instagram.com/satriabelva/) \n"
            "2. *Safila Elsa Vavilya* -> [@safilael](https://www.instagram.com/safilael/)\n"
            "3. Felisita Dian Puspitasari -> [@_dian1234](https://www.instagram.com/_dian1234/)")
st.markdown("- [x] Write the press release")
st.markdown("---")

code = '''
def functionBejo(tes):
    return f'Halo Nama Saya Adalah {tes}'
'''
st.code(code, language='python')
st.write({
    "nama" : "Satria Belva Nararya",
    "Organisasi" : "Himpunan Mahasiswa Sistem Informasi",
    "Skill" : {
        "Bahasa Pemrograman" : ["Python", "Java", "C++"],
        "Bahasa" : ["Indonesia", "Inggris"],
        "Database" : ["MySQL", "MongoDB"]
    }
})

st.image("assets/tes.png",width=400, caption="Ini Adalah Logo HIMASIF", use_container_width=True)
st.divider()
st.image(os.path.join(os.getcwd(), "assets", "tes.png"), caption="Ini Juga Adalah Logo HIMASIF")
st.video("assets/VID-20241025-WA0013.mp4")

st.checkbox(label='Ini adalah checkbox 1', help='This Checkbox will do something in your terminal', value=True, on_change=testingCheckbox, key='tes')
st.checkbox(label='Ini adalah checkbox 2', help='This Clear The Terminal', value=False, on_change=clearTerminal, key='clearTerminal')

st.radio(
    label='Silahkan Pilih Salah Satu Divisi Di Bawah Ini', 
    options=('Kaderisasi', 'Litbang', 'Humas', 'PSDM', 'Mediatek'), 
    captions=('Pengkaderan anggota', 'Penelitian & Pengembangan', 'Hubungan Masyarakat', 'Pengembangan Sumber Daya Mahasiswa', 'Media & Teknologi'),
    help='Choose One of This Divisions Below',
    key='divisi',
    on_change=pilihanDivisi,
    index=3
)

st.selectbox(
    label='Silahkan Pilih Salah Satu Organisasi Di Bawah Ini', 
    options=('BEM', 'HIMATIF', 'HMIF', 'HIMASIF', 'BPM'), 
    placeholder='"Choose an option',
    help='Choose One of This Organization Below',
    on_change=organizationSelection,
    key='organisasi',
    label_visibility='visible',
    index=3
)

st.button(
    label='Click This Button To Clear The Terminal',
    on_click=clearTerminal,
    key='clearTerminalButton',
    icon="🗑️",
    help='Click This Button To Automaticly Clear Your Terminal',
    use_container_width=True,
    type='secondary',
)

st.title('Upload CV Anda')
st.markdown('---')
st.file_uploader(
    label='Upload CV Anda',
    type=['pdf','jpg','png','heic'],
    help='Apabila Anda mendaftar organisasi maka perlu mengupload CV',
    accept_multiple_files=True,
    on_change=previewUploadedFile,
    key='uploadedFile'
)   

st.markdown('---')

st.slider(
    label='Silahkan Pilih Nilai Angka Anda',
    min_value=0.0,
    max_value=100.0,
    step=0.5,
    value=(0.0,20.0),
    key='nilaiAngka',
    help='Silahkan Pilih Nilai Angka Anda'
)

# Contoh yang Salah

st.text_input(
    label='Silahkan Masukkan Username Anda',
    key='username',
    help='Silahkan Masukkan Username Anda',
    type='default',
    max_chars=30,
    placeholder='contoh : @satriabelva',
)

st.text_input(
    label='Silahkan Masukkan Password Anda',
    key='password',
    help='Silahkan Masukkan Password Anda',
    type='password',
)

st.date_input(
    label='Silahkan Pilih Tanggal Lahir Anda',
    key='tanggalLahir',
    help='Silahkan Pilih Tanggal Lahir Anda',
    format='DD/MM/YYYY',
    max_value=datetime.date.today(),
    min_value=datetime.date(1925, 6, 23) 
)

st.text_area(
    label='Silahkan Masukkan Deskripsi Anda',
    key='deskripsi',
    help='Silahkan Masukkan Deskripsi Anda',
    placeholder='Deskripsikan Diri Anda Sedetail Mungkin'
)

st.button(
    label='Submit',
    on_click=usernameAndPassword,
    key='usernameAndPasswordSubmitButton',
    icon="📜",
    help='Click This Button To Submit Your Account',
    use_container_width=True,
    type='secondary',
)


# Contoh Yang Benar 
st.markdown("<h1 style='text-align : center;'>User Registration</h1>", unsafe_allow_html=True)
with st.form(key='form2', clear_on_submit=False, enter_to_submit=False) :
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

x = np.linspace(0,10,100)
y = np.array([1,2,3,4,5,6,7,8,9,10])
z = np.array([1,2,3,4,5,6,7,8,9,10])
opt = st.sidebar.radio(label='Select Any Graph', options=('Line', 'Bar', 'H-Bar'))
if opt == "Line": 
    st.markdown("<h1 style='text-align : center;'>Line Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.plot(x, np.cos(x), '--')
    plt.plot(x, np.sin(x))
    st.write(fig)
elif opt == "Bar" :
    st.markdown("<h1 style='text-align : center;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.bar(y,y*10)
    plt.bar(z,z*5)
    st.write(fig)
else :
    st.markdown("<h1 style='text-align : center;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.barh(y*10,y)
    st.write(fig)

st.markdown('---')