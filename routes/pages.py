import streamlit as st

def get_pages() :
    # === Belajar Pages ===
    Penampungan     = st.Page("view/sandbox/0 Penampungan.py", title="Dashboard", icon=":material/dashboard:")
    Data            = st.Page("view/sandbox/1 Data.py", title="Data Component", icon=":material/folder_open:")
    Charts          = st.Page("view/sandbox/2 Charts.py", title="Charts Component", icon=":material/signal_cellular_alt:")
    Forms           = st.Page("view/sandbox/3 Forms.py", title="Form Component", icon=":material/forms_add_on:")
    Session_State   = st.Page("view/sandbox/4 Session State.py", title="Session State", icon=":material/cookie:")
    Callback        = st.Page("view/sandbox/5 Callback.py", title="Callback", icon=":material/function:")
    Layout          = st.Page("view/sandbox/6 Layout.py", title="Layout", icon=":material/dashboard:")
    Fragment        = st.Page("view/sandbox/7 Fragment.py", title="Fragment", icon=":material/segment:")
    DB_mySQL_Conn   = st.Page("view/sandbox/8 Database Connection (mySQL).py", title="Database Connection (mySQL)", icon=":material/database:")
    DB_Gsheet_Conn  = st.Page("view/sandbox/9 Database Connection (Google Sheet).py", title="Database Connection (Google Sheet)", icon=":material/docs:")
    Gmail_Auth      = st.Page("view/sandbox/10 Gmail Authentication.py", title="Gmail Account Authentication", icon=":material/account_circle:")

    # === Projects Pages ===
    Populytics              = st.Page("view/projects/Populytics.py", title="Populytics", icon=":material/group:", default=True)
    EcoScope                = st.Page("view/projects/EcoScope.py", title="EcoScope", icon=":material/show_chart:")
    ADOIndihome             = st.Page("view/projects/ADOIndihome.py", title="ADO IH", icon=":material/cell_tower:")
    ADOMobile               = st.Page("view/projects/ADOMobile.py", title="ADO Mobile", icon=":material/smartphone:")
    MarketCompetition       = st.Page("view/projects/MarketCompetition.py", title="Market Competition", icon=":material/public:")
    # Market_Radar    = st.Page("view/projects/Market Radar.py", title="Market Radar", icon=":material/shopping_cart:")
    # tes_lagi_2      = st.Page("view/projects/tes_lagi_2.py", title="tes_lagi_2", icon=":material/show_chart:")

    return {
        "Analisis Daerah Operasi": [Populytics, EcoScope, ADOIndihome, ADOMobile, MarketCompetition],
        # "Belajar": [Penampungan,Data,Charts,Forms,Session_State,Callback,Layout,Fragment,DB_mySQL_Conn,DB_Gsheet_Conn,Gmail_Auth]
    }