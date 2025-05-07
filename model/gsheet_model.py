import streamlit as st
from model.db_connection import gsheet_ADOMobile_connection, gsheet_ADOIH_connection

ADOMobileconn = gsheet_ADOMobile_connection()
ADOIHconn = gsheet_ADOIH_connection()

def get_gsheet_ADOMobile_data(): 
    st.header("📗 Data Gsheet ADO Mobile")
    if st.button("Refresh Data", icon='🔁'):
        st.cache_data.clear()

    df = ADOMobileconn.read(ttl=2)
    try:
        st.write(df)
        for row in df.itertuples():
            st.write(f'''
                Regional        : {row.REGIONAL}
                BRANCH          : {row.BRANCH}
                CLUSTER	        : {row.CLUSTER}
                Site  	        : {row.SITE}
                CB  	        : {row.CB}
                Populasi        : {row.POPULASI} Orang\n 
            ''')
        st.write("Kolom-kolom di DataFrame:", df.columns.tolist())
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None
    
def get_gsheet_ADOIH_data(): 
    df = ADOIHconn.read(ttl=2)
    try:
        st.header("📗 Data Gsheet ADO IH")
        for row in df.itertuples():
            st.write(f'''
                Rgional         : {row.REGIONAL}
                BRANCH          : {row.BRANCH}
                CLUSTER	        : {row.WOK}
                Site  	        : {row.KABUPATEN}
                CB  	        : {row.TOTAL_HOUSEHOLD}
                Populasi        : {row.LIS_AKTIF}\n 
            ''')
        st.write("Kolom-kolom di DataFrame:", df.columns.tolist())
    except Exception as e:
        st.error("Gagal mengambil gsheet.")
        st.exception(e)
        return None