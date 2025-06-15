import streamlit as st
from streamlit_gsheets import GSheetsConnection 

def get_connection():
    return st.connection('internship_RLO', type='sql')

def gsheet_ADOMobile_connection() :
    return st.connection("ADOMobile", type=GSheetsConnection)

def gsheet_ADOIH_connection() :
    return st.connection("ADOIH", type=GSheetsConnection)

def gsheet_kondisi_connection() :
    return st.connection("kondisi", type=GSheetsConnection)

def gsheet_MarketCompetition_connection() :
    return st.connection("MarketCompetition", type=GSheetsConnection)