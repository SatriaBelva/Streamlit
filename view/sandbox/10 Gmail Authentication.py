import streamlit as st
import os
from model import *

st.title("Gmail Account Authenticator")
st.text("Pada Page ini kita akan belajar mengenai cara login menggunakan akun gmail berikut adalah caranya :")

st.markdown("### 1. Tonton Video Ini dulu")
st.text('Tutorialnya lumayan lengkap di situ dan cukup lihat sampai menit ke 5:54')
st.video("https://www.youtube.com/watch?v=QziGFxHM1pA&t=54s", autoplay=False, start_time="54s" )

st.markdown("### 2. Tambahkan Kredensial Google Cloud")
st.markdown('Tambahkan kode ini di :gray-background[.streamlit/secrets.toml] untuk menyimpan kredensial google cloud authenticator kamu')
st.code('''
    [auth]
    redirect_uri = "http://localhost:8501/oauth2callback" # Ngga Usah Diganti
    cookie_secret = "your_cookie_secret_here" # Disesuaikan dengan punyamu

    [auth.google] 
    client_id = "your_client_id_here" # Disesuaikan dengan punyamu
    client_secret = "your_client_secret_here" # Disesuaikan dengan punyamu
    server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration" # Ngga Usah Diganti
''', language="python")

st.markdown("### 3. Buat Controller Untuk Authentication")
st.markdown('Silahkan Buka :gray-background[controller/auth_controller.py] dan silahkan buat logika dan alur program untuk mengahndle authentication menggunakan gmail')
st.warning('Sedikit catatan saya membatasi hanya Gmail Account yang saya daftarkan ke database mySQL saya saja yang bisa login. Untuk itu saya membuat sebuah function yang berguna untuk mengambil seluruh email yang sudah saya daftarkan')
col1, col2= st.columns(2)
with col1:
    st.code('''
    # model/account_model.py
    def get_email_data() :
        try:
            return conn.query('SELECT email FROM email;', ttl=600)
        except Exception as e:
            st.error("Gagal mengambil data kontak.")
            st.exception(e)
            return None
    ''')
with col2:
    st.image(os.path.join(os.getcwd(), "assets", "email.png"))
st.markdown('Artinya hanya email email ini yang bisa login ke dalam aplikasi karena nantinya email tersebut akan disimpan dalam sebuah list')
col1, col2, col3 = st.columns([0.3, 0.4, 0.2])
with col1:
    pass
with col2:
    listEmail = []
    for i in get_email_data().itertuples() :
        listEmail.append(i.email)
    st.write(listEmail)
with col3:
    pass


st.markdown('Lanjutkan dengan membuat logika controller')
st.code('''
    # controller/auth_controller.py
    def login():
        user = st.experimental_user
        email = get_email_data()
        authenticated_email = [] # Email yang sudah didaftarkan akan disimpan di sini
        for i in email.itertuples():
                authenticated_email.append(i.email)

        if not user.is_logged_in:
            st.markdown(landing_page_style(), unsafe_allow_html=True)
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        
            # Di sinilah elemen yang penting (HARUS ADA on_click=lambda: st.login("google"))
            st.button("🔐 Login dengan Google", on_click=lambda: st.login("google"), key="login_button") 
            # Sisanya bisa kamu kreasikan sendiri

            st.markdown("</div></div>", unsafe_allow_html=True)
            return False
        else:
            if user.email not in authenticated_email: # Selain email yang sudah didaftarkan tidak akan bisa masuk ke aplikasi
                st.error("⚠️ Maaf, email kamu tidak memiliki akses ke aplikasi ini.")
                st.button("Kembali ke Landing Page", on_click=lambda: st.logout())
                st.markdown(hide_sidebar(), unsafe_allow_html=True)
                return False
            else : 
                st.sidebar.success(f"Hai, {user.name} 👋")
                if st.sidebar.button("Logout"):
                    st.logout()
                return True
    ''')
st.caption("Boleh Copas Boleh berkreasi dengan logikamu sendiri :3")

st.markdown("### 4. Perbarui main.py")
st.markdown('Berhubung :gray-background[main.py] adalah pusat navigasi dari aplikasi maka perlu dibuat logika yang menghandle authenticationnya. Apabila tidak login atau email yang ia gunakan untuk login tidak terdaftar di database maka dia tidak bisa mengakses aplikasinya. Logikanya sesederhana dengan memanggil controller yang berfungsi untuk authentication di halaman main.py')
st.code('''
    # main.py
    from controller import *
    if login() == True :
        # === Belajar Pages ===
        Penampungan     = st.Page("view/belajar/0 Penampungan.py", title="Dashboard", icon=":material/dashboard:")
        Data            = st.Page("view/belajar/1 Data.py", title="Data Component", icon=":material/folder_open:")
        Charts          = st.Page("view/belajar/2 Charts.py", title="Charts Component", icon=":material/signal_cellular_alt:")
        Forms           = st.Page("view/belajar/3 Forms.py", title="Form Component", icon=":material/forms_add_on:")
        Session_State   = st.Page("view/belajar/4 Session State.py", title="Session State", icon=":material/cookie:")
        Callback        = st.Page("view/belajar/5 Callback.py", title="Callback", icon=":material/function:")
        Layout          = st.Page("view/belajar/6 Layout.py", title="Layout", icon=":material/dashboard:")
        Fragment        = st.Page("view/belajar/7 Fragment.py", title="Fragment", icon=":material/segment:")
        DB_mySQL_Conn   = st.Page("view/belajar/8 Database Connection (mySQL).py", title="Database Connection (mySQL)", icon=":material/database:")
        DB_Gsheet_Conn  = st.Page("view/belajar/9 Database Connection (Google Sheet).py", title="Database Connection (Google Sheet)", icon=":material/docs:")
        Gmail_Auth      = st.Page("view/belajar/10 Gmail Authentication.py", title="Gmail Account Authentication", icon=":material/account_circle:")

        # === Projects Pages ===
        Populytics      = st.Page("view/projects/Populytics.py", title="Populytics", icon=":material/group:", default=True)
        Market_Radar    = st.Page("view/projects/Market Radar.py", title="Market Radar", icon=":material/shopping_cart:")
        EcoScope        = st.Page("view/projects/EcoScope.py", title="EcoScope", icon=":material/show_chart:")

        # === Navigation ===
        pg = st.navigation({
            "Project Internship RLO": [Populytics,Market_Radar,EcoScope],
            "Belajar": [Penampungan,Data,Charts,Forms,Session_State,Callback,Layout,Fragment,DB_mySQL_Conn,DB_Gsheet_Conn,Gmail_Auth],
        })
        pg.run()
    else :
        pass
    ''')

st.title("Kredensial Data Akun")
st.markdown("Apabila kamu menggunakan :gray-background[.st.login('google')] maka data data akun gmail yang kamu gunakan untuk login akan disimpan dalam sebuah variabel bernama :gray-background[:green[experimental_user]].\n:gray-background[:green[experimental_user]] merupakan variabel dengan format dictionary dan berisi data data yang akan bisa digunakan di seluruh halaman sehingga cocok untuk session.\n\nIni adalah isi dari variabel :gray-background[:green[experimental_user]]")
st.experimental_user
st.markdown("Oleh karena itu kita bisa memanfaatkan variabel ini untuk keperluan authentication")
st.code('''
    # Email yang sudah didaftarkan di database
    ["elrahmaandini@gmail.com",
     "felisita029@gmail.com",
     "vavilyasafila@gmail.com",
     "bagusilmanhuda@gmail.com",
     "taqiyyah1964ap@gmail.com",
     "satriabelvanararya@gmail.com"]
        
    user = st.experimental_user.email
    # output : satriabelvanararya@gmail.com

    # controller/auth_controller.py
    ...
    if user not in authenticated_email: # Selain email yang sudah didaftarkan tidak akan bisa masuk ke aplikasi
            st.error("⚠️ Maaf, email kamu tidak memiliki akses ke aplikasi ini.")
            st.button("Kembali ke Landing Page", on_click=lambda: st.logout())
            st.markdown(hide_sidebar(), unsafe_allow_html=True)
            return False
    ...
''')
