import streamlit as st
st.set_page_config(
    layout='wide',
    menu_items={
        "Get help": 'mailto:satriabelvanararyan@gmail.com',
        'About': 'Made by Satria Belva Nararya'
    }
)
with st.sidebar:
    st.image("assets\logo_telkomsel.png", width=150)

from routes import *
from middleware import *

if auth_guard() :
    pg = st.navigation(get_pages())
    pg.run()
