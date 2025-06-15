import streamlit as st
from model.db_connection import get_connection

conn = get_connection()

def get_indeks_ekonomi(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT kecamatan.nama AS Kecamatan, 
                SUM(kecamatan.indeks_ekonomi_normalized) AS "Indeks Ekonomi" 
                FROM kecamatan 
                GROUP BY kecamatan.nama
            ''', ttl=600)
        elif kecamatan != "Semua" :
            # return conn.query(f'''
            #     SELECT 
            #         kelurahan.nama AS Kelurahan, 
            #         SUM(kelurahan.tidakbelum_sekolah + kelurahan.belum_tamatSD + kelurahan.tamatSD) AS "Tidak/putus sekolah, belum tamat SD, tamat SD"
            #     FROM kelurahan
            #     JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
            #     WHERE kecamatan.nama = "{kecamatan}"
            #     GROUP BY kelurahan.nama
            #     ''', ttl=600)
            return conn.query(f'''
                SELECT kecamatan.nama AS Kecamatan, 
                SUM(kecamatan.indeks_ekonomi_normalized) AS "Indeks Ekonomi" 
                FROM kecamatan 
                GROUP BY kecamatan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    

def get_DayaBeli(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT kecamatan.nama AS Kecamatan, 
                SUM(kecamatan.daya_Beli_Kecamatan) AS "Daya Beli/ Kecamatan" 
                FROM kecamatan 
                GROUP BY kecamatan.nama
            ''', ttl=600)
        elif kecamatan != "Semua" :
            # return conn.query(f'''
            #     SELECT 
            #         kelurahan.nama AS Kelurahan, 
            #         SUM(kelurahan.tidakbelum_sekolah + kelurahan.belum_tamatSD + kelurahan.tamatSD) AS "Tidak/putus sekolah, belum tamat SD, tamat SD"
            #     FROM kelurahan
            #     JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
            #     WHERE kecamatan.nama = "{kecamatan}"
            #     GROUP BY kelurahan.nama
            #     ''', ttl=600)
            return conn.query(f'''
                SELECT kecamatan.nama AS Kecamatan, 
                SUM(kecamatan.daya_Beli_Kecamatan) AS "Daya Beli/ Kecamatan" 
                FROM kecamatan 
                GROUP BY kecamatan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None