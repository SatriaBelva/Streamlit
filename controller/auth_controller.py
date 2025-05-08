import streamlit as st
from model import *
from utils import *

# Fungsi untuk ambil data user dari session login
def get_current_user():
    # Jika login manual
    if "manual_user" in st.session_state:
        return type("User", (), {
            "is_logged_in": True,
            "email": st.session_state["manual_user"]["email"],
            "name": st.session_state["manual_user"]["name"]
        })()

    user = st.experimental_user

    if user is None:
        st.info("🔄 Menunggu data login Google...")
        st.stop()

    if user and "email" in user:
        return type("User", (), {
            "is_logged_in": True,
            "email": user["email"],
            "name": user.get("name", "No Name")
        })()

    return type("User", (), {
        "is_logged_in": False,
        "email": None,
        "name": None
    })()
    # Jika login manual
    # if "manual_user" in st.session_state:
    #     return type("User", (), {
    #         "is_logged_in": True,
    #         "email": st.session_state["manual_user"]["email"],
    #         "name": st.session_state["manual_user"]["name"]
    #     })()

    # # Jika login Google
    # user = st.experimental_user
    # if user and "email" in user:
    #     return type("User", (), {
    #         "is_logged_in": True,
    #         "email": user["email"],  # Akses email via key
    #         "name": user.get("name", "No Name")  # Periksa jika name ada
    #     })()

    # # Jika belum login
    # return type("User", (), {
    #     "is_logged_in": False,
    #     "email": None,
    #     "name": None
    # })()
    # return st.experimental_user

# Fungsi untuk ambil daftar email yang diizinkan dari database
def get_allowed_emails():
    email_data = get_email_data()
    return [row.email for row in email_data.itertuples()]

# Fungsi untuk mengecek apakah email user termasuk dalam daftar yang diizinkan
def is_email_allowed(email: str) -> bool:
    allowed_emails = get_allowed_emails()
    return email in allowed_emails

# Komponen UI untuk login
def render_login_page():
    # landing_page_style()
    st.markdown(hide_tools(), unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

    with col1:
        pass
    with col2:
        st.markdown("### 🔑 Login Manual")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login Manual"):
            user = validate_manual_login(email, password)
            if user:
                st.session_state["manual_user"] = user
                st.rerun()
            else:
                st.error("Email atau password salah.")

        # st.markdown("### 🔐 Login dengan Google")
        # st.button("Login dengan Google", use_container_width=False, on_click=lambda: st.login("google"), key="login_button")
    with col3:
        pass
    # landing_page_style()
    # st.markdown(hide_tools(), unsafe_allow_html=True)
    # col1, col2 = st.columns(2) 
    # with col1 :
    #     st.button("🔐 Login dengan Google",use_container_width=True, on_click=lambda: st.login("google"), key="login_button")
    # with col2 :
    #     st.button("hello")
    # st.markdown("</div></div>", unsafe_allow_html=True)
    # st.markdown(landing_page_style(), unsafe_allow_html=True)
    # st.markdown(landing_page(), unsafe_allow_html=True)

# Komponen UI untuk user yang tidak diizinkan
def render_unauthorized_page():
    st.error("⚠️ Maaf, email kamu tidak memiliki akses ke aplikasi ini.")
    st.button("Kembali ke Landing Page", on_click=lambda: st.logout())
    st.markdown(hide_sidebar(), unsafe_allow_html=True)

# Komponen greeting dan logout sidebar
def render_sidebar_greeting(user):
    st.sidebar.success(f"Hai, {user.name} 👋")
    if st.sidebar.button("Logout"):
        st.session_state.pop("manual_user", None)
        st.logout()
    # st.sidebar.success(f"Hai, {user.name} 👋")
    # if st.sidebar.button("Logout"):
    #     st.logout()

def validate_manual_login(email, password):
    df = get_account_data()
    if df is None:
        return None

    for row in df.itertuples():
        if row.email == email and row.password == password:
            return {
                "email": row.email,
                "name": row.email.split("@")[0].title()  # Atau simpan nama jika tersedia
            }
    return None


























# def login():
#     user = st.experimental_user
#     email = get_email_data()
#     authenticated_email = []
#     for i in email.itertuples():
#             authenticated_email.append(i.email)

#     if not user.is_logged_in:
#         st.markdown(landing_page_style(), unsafe_allow_html=True)
#         st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
#         st.button("🔐 Login dengan Google", on_click=lambda: st.login("google"), key="login_button")
#         st.markdown("</div></div>", unsafe_allow_html=True)
#         return False
#     else:
#         if user.email not in authenticated_email:
#             st.error("⚠️ Maaf, email kamu tidak memiliki akses ke aplikasi ini.")
#             st.button("Kembali ke Landing Page", on_click=lambda: st.logout())
#             st.markdown(hide_sidebar(), unsafe_allow_html=True)
#             return False
#         else : 
#             st.sidebar.success(f"Hai, {user.name} 👋")
#             if st.sidebar.button("Logout"):
#                 st.logout()
#             return True