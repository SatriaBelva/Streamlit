import streamlit as st
import pandas as pd
import numpy as np
from controller import *
from model import *

# =================================================================================
# BAGIAN INI HANYA UNTUK DEMONSTRASI (DATA DUMMY)
# Ganti dengan pemanggilan fungsi asli Anda yang mengambil data dari model.
# Data dummy ini dibuat untuk memastikan semua 4 kondisi bisa diuji.
# =================================================================================
# def get_Kabupaten_data():
#     return ["Lumajang", "Jember", "Bondowoso", "Situbondo"]

# def get_PENETRATION_RATE():
#     # Asumsi: [Rendah, Rendah, Tinggi, Tinggi]
#     return [0.25, 0.40, 0.85, 0.75]

# def get_PORT_SHARE():
#     # Asumsi: [Tinggi, Rendah, Tinggi, Rendah]
#     return [0.80, 0.30, 0.90, 0.40]
# =================================================================================
# AKHIR BAGIAN DATA DUMMY
# =================================================================================

def get_strategy_content():
    """
    Mengambil data strategi dari berbagai fungsi sumber dan mengubahnya 
    menjadi format dictionary yang terstruktur.
    """
    try:
        # Membuat DataFrame dari setiap fungsi get_*
        df_strategy = pd.DataFrame({
            'Kondisi'      : get_Kondisi_data(),
            'Emoji'        : get_Emoji_data(),
            'Judul'        : get_Judul_data(),
            'Interpretasi' : get_Interpretasi_data(),
            'Strategi'     : get_Strategi_data(),
        })
        
        if df_strategy.empty:
            st.error("Data strategi kosong atau gagal dimuat.")
            return None

        content = {}
        for _, row in df_strategy.iterrows():
            kondisi = row['Kondisi']
            content[kondisi] = {
                "emoji": row['Emoji'],
                "title": row['Judul'],
                "interpretation": row['Interpretasi'],
                # Memisahkan string strategi menjadi list berdasarkan baris baru
                "strategies": row['Strategi'].strip().split('\n') if isinstance(row['Strategi'], str) else []
            }
        
        return content
    except Exception as e:
        st.error(f"Gagal mengambil atau memproses data strategi: {e}")
        return None

def determine_condition(penetration, port_share, pen_threshold=0.10, port_threshold=0.40):
    """
    Menentukan kondisi (A, B, C, D) berdasarkan nilai penetration dan port share.
    Ambang batas (threshold) telah diperbarui sesuai aturan baru.
    """
    if pd.isna(penetration) or pd.isna(port_share):
        return None

    if penetration < pen_threshold and port_share >= port_threshold:
        return "A"  # Kondisi A: Rendah (<10%), Tinggi (>=40%)
    elif penetration < pen_threshold and port_share < port_threshold:
        return "B"  # Kondisi B: Rendah (<10%), Rendah (<40%)
    elif penetration >= pen_threshold and port_share >= port_threshold:
        return "C"  # Kondisi C: Tinggi (>=10%), Tinggi (>=40%)
    elif penetration >= pen_threshold and port_share < port_threshold:
        return "D"  # Kondisi D: Tinggi (>=10%), Rendah (<40%)
    else:
        return None

def display_strategy_ui():
    """
    Fungsi utama untuk membangun dan menampilkan UI Streamlit.
    """
    strategy_content = get_strategy_content()
    if not strategy_content:
        return

    try:
        df = pd.DataFrame({   
            'Kabupaten'        : get_Kabupaten_data(),
            'Penetration Rate' : get_PENETRATION_RATE(),
            'Port Share'       : get_PORT_SHARE(),
        })
        
        # Menyamakan nama kolom ke format standar
        column_mapping = {
            'KABUPATEN': 'Kabupaten',
            'PENETRATION RATE': 'Penetration Rate',
            'PORT SHARE': 'Port Share'
        }
        df.rename(columns=lambda c: column_mapping.get(c.upper(), c), inplace=True)

        required_cols = ['Kabupaten', 'Penetration Rate', 'Port Share']
        if not all(col in df.columns for col in required_cols):
            st.error(f"DataFrame yang dibuat harus memiliki kolom: {', '.join(required_cols)}. Kolom yang ditemukan: {list(df.columns)}")
            return
        
        # --- LANGKAH DIAGNOSIS 1: Tampilkan data mentah ---
        # with st.expander("Lihat Data Mentah (Sebelum diproses)"):
        #     st.dataframe(df)
            
        # Proses pembersihan data
        for col in ['Penetration Rate', 'Port Share']:
            df[col] = df[col].astype(str).str.replace(',', '.', regex=False).str.replace('%', '', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')
            if not df[col].empty and not df[col].isna().all() and df[col].max() > 1:
                df[col] = df[col] / 100.0

    except Exception as e:
        st.error(f"Gagal memproses DataFrame: {e}")
        return

    col1, _ = st.columns([1, 3])
    with col1:
        valid_kabupaten_df = df.dropna(subset=['Penetration Rate', 'Port Share'])
        if valid_kabupaten_df.empty:
            st.error("Tidak ada data kabupaten yang valid untuk ditampilkan. Periksa kembali format data sumber.")
            return

        selected_kabupaten = st.selectbox(
            "Pilih Kab/Kota",
            valid_kabupaten_df['Kabupaten'].unique(),
            label_visibility="collapsed",
            key="strategy_selectbox_main"
        )
    
    st.write("") 

    if selected_kabupaten:
        kab_data = df[df['Kabupaten'] == selected_kabupaten].iloc[0]
        penetration = kab_data['Penetration Rate']
        port_share = kab_data['Port Share']
        

        condition_key = determine_condition(penetration, port_share)
        
        if condition_key and condition_key in strategy_content:
            content = strategy_content[condition_key]
            st.subheader(f"{content['emoji']} {selected_kabupaten}")
            st.markdown("**Interpretasi:**")
            st.info(content['interpretation'])
            st.markdown("**Strategi Umum:**")
            for strategy in content['strategies']:
                st.markdown(f"- {strategy}")
        else:
            st.warning(f"Data untuk {selected_kabupaten} tidak lengkap atau tidak valid untuk menentukan kondisi.")
