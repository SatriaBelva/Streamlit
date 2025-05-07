import streamlit as st
from model.db_connection import get_connection

conn = get_connection()

def get_kecamatan_data() :
    try:
        return conn.query('SELECT nama FROM kecamatan;', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
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
    