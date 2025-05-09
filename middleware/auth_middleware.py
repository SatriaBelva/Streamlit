from controller import *
from routes import *

# def auth_guard():
#     user = get_current_user()

#     if not user.is_logged_in:
#         render_login_page()
#         return False

#     if not is_email_allowed(user.email):
#         render_unauthorized_page()
#         return False

#     render_sidebar_greeting(user)
#     return True

def auth_guard():
    try:
        user = get_current_user()
        if user is None:
            st.error("❌ Gagal mendapatkan user (user is None)")
            render_login_page()
            return False

        # st.info(f"👤 User terdeteksi: {user.email if hasattr(user, 'email') else 'Tidak ada email'}")

        if not user.is_logged_in:
            # st.warning("⚠️ User belum login.")
            render_login_page()
            return False

        if not is_email_allowed(user.email):
            st.warning("⛔ Email tidak diizinkan.")
            render_unauthorized_page()
            return False

        render_sidebar_greeting(user)
        return True

    except Exception as e:
        st.error(f"❌ Terjadi error saat autentikasi: {e}")
        return False
