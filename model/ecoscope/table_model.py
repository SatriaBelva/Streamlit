import streamlit as st
from model.db_connection import get_connection

conn = get_connection()

@st.cache_data
def get_kecamatan_data() :
    try:
        return conn.query('SELECT nama FROM kecamatan;', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None

@st.cache_data    
def get_jumlah_penduduk_data(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT kecamatan.nama as kecamatan, SUM(kelurahan.jumlah_penduduk) as "Jumlah Penduduk" 
                FROM kelurahan 
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID 
                GROUP BY kecamatan.nama 
                ''', ttl=600)
        elif kecamatan != "Semua" :
            return conn.query(f'''
                SELECT kecamatan.nama as kecamatan, SUM(kelurahan.jumlah_penduduk) as "Jumlah Penduduk" 
                FROM kelurahan 
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID 
                GROUP BY kecamatan.nama 
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None

@st.cache_data
def get_indeks_ekonomi_table() :
    try:
        return conn.query('''
            SELECT kecamatan.nama, kecamatan.indeks_ekonomi_normalized AS "Indeks Ekonomi"
            FROM kecamatan
        ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None

@st.cache_data    
def get_kategori_ekonomi_data() :
    try:
        return conn.query('''
            SELECT kecamatan.nama, kecamatan.tingkat_ekonomi AS "Kategori Ekonomi"
            FROM kecamatan
        ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None

@st.cache_data
def get_kategori_Pelajar_Mahasiswa() :
    try:
        return conn.query('''
            SELECT kecamatan.nama, kecamatan.Pelajar_Mahasiswa AS "Pelajar Mahasiswa"
            FROM kecamatan
        ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None

@st.cache_data    
def get_kategori_IRT() :
    try:
        return conn.query('''
            SELECT kecamatan.nama, kecamatan.IRT AS "IRT"
            FROM kecamatan
        ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None

@st.cache_data    
def get_kategori_Nelayan_Perdagangan_Wiraswasta() :
    try:
        return conn.query('''
            SELECT kecamatan.nama, kecamatan.Nelayan_Perdagangan_Wiraswasta AS "Nelayan Perdagangan Wiraswasta"
            FROM kecamatan
        ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None

@st.cache_data    
def get_kategori_Guru_Perawat_Pengacara() :
    try:
        return conn.query('''
            SELECT kecamatan.nama, kecamatan.Guru_Perawat_Pengacara AS "Guru Perawat Pengacara"
            FROM kecamatan
        ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None

@st.cache_data    
def get_kategori_Total_Usia_Produktif() :
    try:
        return conn.query('''
            SELECT kecamatan.nama, kecamatan.Total_Usia_Produktif AS "Total Usia Produktif"
            FROM kecamatan
        ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
@st.cache_data   
def get_kategori_Daya_Beli_Kecamatan() :
    try:
        return conn.query('''
            SELECT kecamatan.nama, kecamatan.Daya_Beli_Kecamatan AS "Daya Beli/Kecamatan"
            FROM kecamatan
        ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None