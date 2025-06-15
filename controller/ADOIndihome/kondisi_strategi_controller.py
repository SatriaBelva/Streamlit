import streamlit as st
import pandas as pd
from model import *

def get_strategy_from_gsheet():
    """
    Mengambil data strategi dari Google Sheet dan mengubahnya menjadi format dictionary.
    """
    try:
        # Ganti 'Strategi' dengan nama sheet Anda yang sebenarnya jika berbeda
        df_strategy = get_Strategi('Strategi') 
        
        if df_strategy.empty:
            st.error("Data strategi dari Google Sheet kosong atau gagal dimuat.")
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
        st.error(f"Gagal mengambil atau memproses data strategi dari Google Sheet: {e}")
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
    st.title("Capacity & Expansion Insight")
    st.caption("Mengkombinasikan Penetration Rate dan Available PORT Share untuk mengklasifikasikan kondisi wilayah.")
    st.divider()
    
    # Mengambil konten strategi dari Google Sheet
    strategy_content = get_strategy_from_gsheet()
    if not strategy_content:
        return # Menghentikan eksekusi jika data strategi gagal dimuat

    try:
        df = pd.DataFrame({   
            'Kabupaten'        : get_Kabupaten_data(),
            'Penetration Rate' : get_PENETRATION_RATE(),
            'Port Share'       : get_PORT_SHARE(),
        })
        
        for col in ['Penetration Rate', 'Port Share']:
            df[col] = df[col].astype(str).str.replace(',', '.', regex=False).str.replace('%', '', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')
            if not df[col].empty and not df[col].isna().all() and df[col].max() > 1:
                df[col] = df[col] / 100.0
        
    except Exception as e:
        st.error(f"Gagal memuat atau memproses data kabupaten: {e}")
        return

    col1, _ = st.columns([1, 3])
    with col1:
        valid_kabupaten_df = df.dropna(subset=['Penetration Rate', 'Port Share'])
        if valid_kabupaten_df.empty:
            st.error("Tidak ada data kabupaten yang valid untuk ditampilkan. Periksa kembali format data sumber.")
            return

        selected_kabupaten = st.selectbox("Pilih Kab/Kota", valid_kabupaten_df['Kabupaten'].unique(), label_visibility="collapsed")
    
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