import streamlit as st
st.set_page_config(
    layout='wide',
    menu_items={
        "Get help": 'mailto:satriabelvanararyan@gmail.com',
        'About': 'Made by Satria Belva Nararya'
    }
)
# with st.sidebar:
#     st.image("assets/logo_telkomsel.png", width=150)

from routes import *
from middleware import *

if auth_guard() :
    st.markdown("""
    <style>
    [data-testid="stNavSectionHeader"] {
        font-size: 20px !important;
        text-align: center;
        font-weight: bold !important;
        color: black !important;
        font-family: 'Poppins', sans-serif !important;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    pg = st.navigation(get_pages())
    pg.run()

