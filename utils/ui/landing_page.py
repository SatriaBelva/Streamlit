import base64
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu 

def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_telkomsel = get_base64_image("assets/logo_telkomsel.png")
bg_telkomsel   = get_base64_image("assets/bg_telkomsel.png")
peta           = get_base64_image("assets/peta.png")
Populytics     = get_base64_image("assets/Populytics.png")
EcoScope       = get_base64_image("assets/EcoScope.png")
ADOIH          = get_base64_image("assets/ADOIH.png")
ADOMobile      = get_base64_image("assets/ADOMobile.png")

def landing_page_style() :
    html = '''
        <style>
        @keyframes slideUp {
            0% {
                transform: translateY(50px);
                opacity: 0;
            }
            100% {
                transform: translateY(0);
                opacity: 1;
            }
        }
        body {
            background-color: rgba(255, 255, 255, 1);
            width: 100%;
            margin: 0;
        }
        nav{
            /* height: 80px; */
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 18px 75px;
        }
        .navbar-button{
            display: flex;
            gap: 50px;
            font-family: Poppins;
            font-weight: 600;
        }

        .navbar-button a{
            color: rgba(20, 23, 31, 1);
            text-decoration: none;
        }

        .landing-page {
            position: relative;
            height: 41vh;
            overflow: hidden;
            padding: 0 75px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            z-index: 1;
            margin-bottom:80px;
            animation: slideUp 2s ease-out;
        }

        .telkomsel-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 41vh;
            object-fit: cover;
            z-index: -1;
            animation: slideUp 2s ease-out;
        }

        .landing-page h1 {
            font-family: Inter;
            font-weight: 800;
            font-size: 120px;
            margin: 0 0 30px 0;
            z-index: 1;
            animation: slideUp 2s ease-out;
        }

        .landing-page a {
            z-index: 1;
            width: fit-content;
            background-color: rgba(227, 5, 17, 1);
            border-radius: 16px;
            padding: 20px 24px;
            text-decoration: none;
            animation: slideUp 2s ease-out;
        }

        .landing-page a div {
            font-family: Poppins;
            font-weight: 700;
            font-size: 24px;
            line-height: 24px;
            color: white;
        }


        .hero {
            margin-left: 300px;
            position: relative;
            width: 884px;
            height: 687px;
            background-size: cover;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 5%;
            box-sizing: border-box;
            animation: slideUp 1s ease-out;
        }

        .info-box {
            background-color: #b32025;
            color: white;
            padding: 30px;
            width: 380px;
            border-radius: 10px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
            margin-right: -200px;
        }

        .info-box h1 {
            font-family: Poppins;
            margin: 0 0 20px 0;
            font-size: 32px;
        }

        .info-box p {
            font-family: Poppins;
            font-size: 16px;
            line-height: 1.6;
        }

        @media (max-width: 768px) {
            .hero {
                justify-content: center;
                padding: 20px;
            }

            .info-box {
                width: 100%;
                max-width: 90%;
            }
        }

        .feature {
            text-align: center;
            font-family: 'Poppins', sans-serif;
            padding: 50px 0;
        }

        .feature h1 {
            font-size: 40px;
            font-weight: 700;
            color: #1e1e1e;
            margin-bottom: 40px;
        }

        .cards {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 30px;
        }

        .card {
            background: white;
            border-radius: 20px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
            padding: 30px;
            width: 260px;
            text-align: center;
            transition: transform 0.3s;
            text-decoration: none;
            
        }

        .card:hover {
            transform: translateY(-10px);
        }

        .card .icon {
            width: 60px;
            margin-bottom: 20px;
        }

        .card h3 {
            margin: 0;
            font-size: 20px;
            font-weight: 600;
            color: #1e1e1e;
        }

        .card p {
            font-size: 14px;
            color: #5e5e5e;
            margin-top: 10px;
        }
    </style>'''
    tes = f'''
    {html}
    <nav>
        <img src="data:image/png;base64,{logo_telkomsel}" alt="">
        <div class="navbar-button">
            <a href="#">Beranda</a>
            <a href="#">Fitur</a>
            <a style="color: rgba(249, 153, 93, 1);" href="#">Login</a>
        </div>
    </nav>
    <div class="landing-page">
        <img class="telkomsel-bg" src="data:image/png;base64,{bg_telkomsel}" alt="">
        <h1>Market Analytics</h1>

    </div>
    <section class="hero" data-aos="fade-up" data-aos-duration="1000" style="background: url('data:image/png;base64,{peta}') no-repeat center center;">
        <div class="info-box">
          <h1>Market Analytics</h1>
          <p>Analisis data Kabupaten Jember untuk mendukung pengembangan bisnis  PT. Telekomunikasi Selular Jember  melalui visualisasi data interaktif dalam bentuk peta, grafik, serta rekomendasi  layanan product dan strategi pemasaran di setiap wilayah Kabupaten Jember.</p>

        </div>
    </section>
    <div class="feature" data-aos="fade-up" data-aos-duration="1000">
        <h2>Feature</h2>
        <h1>Kategori Data</h1>
        <div class="cards">
            <div class="card">
                <img src="data:image/png;base64,{Populytics}" class="icon">
                <h3>Populytics</h3>
                <p>Analisis IPM wilayah untuk strategi produk yang sesuai dengan kebutuhan wilayah</p>
            </div>
            <div class="card">
                <img src="data:image/png;base64,{EcoScope}" class="icon">
                <h3>EcoScope</h3>
                <p>Analisis tingkat ekonomi untuk menunjang strategi pemasaran yang efektif</p>
            </div>
            <div class="card">
                <img src="data:image/png;base64,{ADOIH}" class="icon">
                <h3>ADO IH</h3>
                <p>Analisis infrastruktur IndiHome untuk perluasan jaringan yang tepat sasaran</p>
            </div>
            <div class="card">
                <img src="data:image/png;base64,{ADOMobile}" class="icon">
                <h3>ADO Mobile</h3>
                <p>Analisis layanan seluler untuk strategi penetrasi pasar yang efisien</p>
            </div>
        </div>
    </div>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init();
    </script>
    '''
    return components.html(tes, scrolling=False, height=2500)


def hide_sidebar():
    css = """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }

    #MainMenu{
        display: none;
    }

    .stAppDeployButton{
        display: none;
    }
    </style>
    """
    return css

# def landing_page_style() :             
#     css = """
#     <style>
#     /* Gradient background */
#     .landing-container {
#         background: linear-gradient(135deg, #f3f4f6, #e0f7fa);
#         padding: 50px;
#         border-radius: 20px;
#         box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
#         text-align: center;
#         margin-top: 100px;
#     }

#     .landing-title {
#         font-size: 40px;
#         font-weight: 700;
#         color: #0d47a1;
#     }

#     .landing-subtitle {
#         font-size: 18px;
#         color: #333333;
#         margin-top: 10px;
#         margin-bottom: 30px;
#     }

#     .login-button {
#         background-color: #4285F4;
#         color: white;
#         padding: 12px 30px;
#         font-size: 16px;
#         font-weight: bold;
#         border: none;
#         border-radius: 10px;
#         cursor: pointer;
#         box-shadow: 0 4px 14px rgba(66, 133, 244, 0.4);
#         transition: background-color 0.3s ease;
#     }

#     .login-button:hover {
#         background-color: #3367d6;
#     }

#     [data-testid="stSidebar"] {
#         display: none;
#     }

#     [data-testid="stSidebarCollapsedControl"] {
#         display: none;
#     }

#     #MainMenu{
#         display: none;
#     }

#     .stAppDeployButton{
#         display: none;
#     }

#     </style>

#     <div class="landing-container">
#         <div class="landing-title">👋 Selamat Datang di Aplikasi Internship</div>
#         <div class="landing-subtitle">
#             Eksplorasi data, visualisasi, dan manajemen proyek <br>
#             dalam satu dashboard interaktif.
#         </div>

#     """
#     return css