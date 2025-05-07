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

def get_kelurahan_data(kecamatan) :
    try:
        return conn.query(f'''
            SELECT kelurahan.nama 
            FROM kelurahan 
            JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
            WHERE kecamatan.nama = '{kecamatan}'
            ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None