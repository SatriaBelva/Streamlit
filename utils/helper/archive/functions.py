import os
import streamlit as st

def clearTerminal():
    if st.session_state.get("clearTerminal", False) or st.session_state.get("clearTerminalButton", False):
        os.system('cls' if os.name == 'nt' else 'clear')

def testingCheckbox():
    """Fungsi untuk mengecek status checkbox di Streamlit."""
    if st.session_state.get("tes", False):
        print('Anda sudah benar')
    else:
        print('Anda salah')

def pilihanDivisi():
    """Menampilkan divisi yang dipilih oleh pengguna."""
    divisi = st.session_state.get("divisi", "")
    print(f'Anda Memilih Divisi {divisi}')

def organizationSelection():
    """Menampilkan organisasi yang dipilih oleh pengguna."""
    organisasi = st.session_state.get("organisasi", "")
    print(f'Anda Memilih organisasi {organisasi}')

def previewUploadedFile():
    file = st.session_state.get("uploadedFile")
    if file:
        for file in file:
            # if file.name
            print(f"""file id : {file.file_id}\n
                      Judul : {file.name}\n
                      Tipe : {file.type}\n
                      Ukuran : {file.size} Byte\n""") 
            
def usernameAndPassword():
    button = st.session_state.get('usernameAndPasswordSubmitButton')
    username = st.session_state.get('username')
    password = st.session_state.get('password')
    tanggalLahir = st.session_state.get('tanggalLahir')
    deskripsi = st.session_state.get('deskripsi')

    if username and password and tanggalLahir and deskripsi:
        day = tanggalLahir.day
        month = tanggalLahir.strftime("%B")  # Nama bulan dalam bahasa Inggris
        year = tanggalLahir.year
        formatted_date = f"{day} {month} {year}"
        print(f"Username : {username}\nPassword : {password}\nTTL : {formatted_date}\nDeskripsi Diri : {deskripsi}\n")

def registration():
    tes = st.session_state.get('registration')
    if tes:
        # st.write(f"Data dari session_state: {tes}")  # Menampilkan di UI Streamlit
        print(tes)  # Untuk debugging di terminal
    else:
        st.warning("Belum ada data registrasi.")