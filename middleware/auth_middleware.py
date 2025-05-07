from controller import *
from routes import *

def auth_guard():
    user = get_current_user()

    if not user.is_logged_in:
        render_login_page()
        return False

    if not is_email_allowed(user.email):
        render_unauthorized_page()
        return False

    render_sidebar_greeting(user)
    return True