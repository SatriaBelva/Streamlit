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
    
def get_belum_sekolah_data(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT 
                    kecamatan.nama AS Kecamatan, 
                    SUM(kelurahan.tidakbelum_sekolah + kelurahan.belum_tamatSD + kelurahan.tamatSD) AS "Tidak/putus sekolah, belum tamat SD, tamat SD"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                GROUP BY kecamatan.nama;
            ''', ttl=600)
        elif kecamatan != "Semua" :
            return conn.query(f'''
                SELECT 
                    kelurahan.nama AS Kelurahan, 
                    SUM(kelurahan.tidakbelum_sekolah + kelurahan.belum_tamatSD + kelurahan.tamatSD) AS "Tidak/putus sekolah, belum tamat SD, tamat SD"
                FROM kelurahan
                JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
                WHERE kecamatan.nama = "{kecamatan}"
                GROUP BY kelurahan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
def get_SLTPSLTA_data(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT 
                    kecamatan.nama AS Kecamatan, 
                    SUM(kelurahan.SLTP + kelurahan.SLTA) AS "SLTP/SLTA"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                GROUP BY kecamatan.nama;
                ''', ttl=600)
        elif kecamatan != "Semua" :
            return conn.query(f'''
                SELECT 
                    kelurahan.nama AS Kelurahan, 
                    SUM(kelurahan.SLTP + kelurahan.SLTA) AS "SLTP/SLTA"
                FROM kelurahan
                JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
                WHERE kecamatan.nama = "{kecamatan}"
                GROUP BY kelurahan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
    
def get_kuliah_data(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT 
                    kecamatan.nama AS Kecamatan, 
                    SUM(kelurahan.D1_D2 + kelurahan.D3 + kelurahan.S1 + kelurahan.S2 + kelurahan.S3) AS "kuliah"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                GROUP BY kecamatan.nama;
                ''', ttl=600)
        elif kecamatan != "Semua" :
            return conn.query(f'''
                SELECT 
                    kelurahan.nama AS Kelurahan, 
                    SUM(kelurahan.D1_D2 + kelurahan.D3 + kelurahan.S1 + kelurahan.S2 + kelurahan.S3) AS "kuliah"
                FROM kelurahan
                JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
                WHERE kecamatan.nama = "{kecamatan}"
                GROUP BY kelurahan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
def get_firstCategory_data(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT 
                    kecamatan.nama AS Kecamatan, 
                    SUM(kelurahan.belumtidak_kerja + kelurahan.pelajar_mahasiswa + kelurahan.IRT + kelurahan.pensiunan) AS "Category 1"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                GROUP BY kecamatan.nama;
                ''', ttl=600)
        elif kecamatan != "Semua" :
            return conn.query(f'''
                SELECT 
                    kelurahan.nama AS Kelurahan, 
                    SUM(kelurahan.belumtidak_kerja + kelurahan.pelajar_mahasiswa + kelurahan.IRT + kelurahan.pensiunan) AS "Category 1"
                FROM kelurahan
                JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
                WHERE kecamatan.nama = "{kecamatan}"
                GROUP BY kelurahan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
def get_secondCategory_data(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT 
                    kecamatan.nama AS Kecamatan, 
                    SUM(kelurahan.perdagangan + kelurahan.wiraswasta + kelurahan.nelayan) AS "Category 2"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                GROUP BY kecamatan.nama;
                ''', ttl=600)
        elif kecamatan != "Semua" :
            return conn.query(f'''
                SELECT 
                    kelurahan.nama AS Kelurahan, 
                    SUM(kelurahan.perdagangan + kelurahan.wiraswasta + kelurahan.nelayan) AS "Category 2"
                FROM kelurahan
                JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
                WHERE kecamatan.nama = "{kecamatan}"
                GROUP BY kelurahan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
def get_ThirdCategory_data(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT 
                    kecamatan.nama AS Kecamatan, 
                    SUM(kelurahan.guru + kelurahan.perawat + kelurahan.pengacara) AS "Category 3"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                GROUP BY kecamatan.nama;
                ''', ttl=600)
        elif kecamatan != "Semua" :
            return conn.query(f'''
                SELECT 
                    kelurahan.nama AS Kelurahan, 
                    SUM(kelurahan.guru + kelurahan.perawat + kelurahan.pengacara) AS "Category 3"
                FROM kelurahan
                JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
                WHERE kecamatan.nama = "{kecamatan}"
                GROUP BY kelurahan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
def get_jumlah_penduduk_popultycs_data(kecamatan) :
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
                SELECT kelurahan.nama as kelurahan, SUM(kelurahan.jumlah_penduduk) as "Jumlah Penduduk"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                WHERE kecamatan.nama = "{kecamatan}"
                GROUP BY kelurahan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    
def get_jumlahKK_data(kecamatan) :
    try:
        if kecamatan == "Semua" : 
            return conn.query('''
                SELECT kecamatan.nama as kecamatan, SUM(kelurahan.jumlah_KK) as "Jumlah Kartu Keluarga"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                GROUP BY kecamatan.nama 
                ''', ttl=600)
        elif kecamatan != "Semua" :
            return conn.query(f'''
                SELECT kelurahan.nama as kelurahan, SUM(kelurahan.jumlah_KK) as "Jumlah Kartu Keluarga"
                FROM kelurahan
                JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
                WHERE kecamatan.nama = "{kecamatan}"
                GROUP BY kelurahan.nama
                ''', ttl=600)
    except Exception as e:
        st.error("Gagal mengambil data")
        st.exception(e)
        return None
    

    
# def get_kuliah_data_by_kecamatan(kecamatan):
#     try:
#         return conn.query(f'''
#         SELECT 
#             kelurahan.nama AS Kecamatan, 
#             SUM(kelurahan.D1_D2 + kelurahan.D3 + kelurahan.S1 + kelurahan.S2 + kelurahan.S3) AS "kuliah"
#         FROM kelurahan
#         JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
#         WHERE kecamatan.nama = "{kecamatan}"
#         GROUP BY kelurahan.nama
#         ''', ttl=600)
#     except Exception as e:
#         st.error("Gagal mengambil data")
#         st.exception(e)
#         return None

# def get_belum_sekolah_data() :
#     try:
#         return conn.query('''
#         SELECT 
#             kecamatan.nama AS Kecamatan, 
#             kelurahan.KecamatanID,
#             SUM(kelurahan.tidakbelum_sekolah + kelurahan.belum_tamatSD + kelurahan.tamatSD) AS "Tidak/putus sekolah, belum tamat SD, tamat SD"
#         FROM kelurahan
#         JOIN kecamatan ON kelurahan.KecamatanID = kecamatan.KecamatanID
#         GROUP BY kelurahan.KecamatanID, kecamatan.nama;
#         ''', ttl=600)
#     except Exception as e:
#         st.error("Gagal mengambil data")
#         st.exception(e)
#         return None
    
# def get_belum_sekolah_data_by_kecamatan(kecamatan) :
#     try:
#         return conn.query(f'''
#         SELECT 
#             kelurahan.nama AS Kecamatan, 
#             SUM(kelurahan.tidakbelum_sekolah + kelurahan.belum_tamatSD + kelurahan.tamatSD) AS "Tidak/putus sekolah, belum tamat SD, tamat SD"
#         FROM kelurahan
#         JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
#         WHERE kecamatan.nama = "{kecamatan}"
#         GROUP BY kelurahan.nama
#         ''', ttl=600)
#     except Exception as e:
#         st.error("Gagal mengambil data")
#         st.exception(e)
#         return None

# def get_SLTPSLTA_data_by_kecamatan(kecamatan) :
#     try:
#         return conn.query(f'''
#         SELECT 
#             kelurahan.nama AS Kecamatan, 
#             SUM(kelurahan.SLTP + kelurahan.SLTA) AS "SLTP/SLTA"
#         FROM kelurahan
#         JOIN kecamatan ON kecamatan.KecamatanID = kelurahan.KecamatanID
#         WHERE kecamatan.nama = "{kecamatan}"
#         GROUP BY kelurahan.nama
#         ''', ttl=600)
#     except Exception as e:
#         st.error("Gagal mengambil data")
#         st.exception(e)
#         return None