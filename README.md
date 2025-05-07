# 📊 Internship RLO Dashboard

**Internship RLO Dashboard** adalah dashboard market analyst untuk Telkomsel Jember yang memudahkan analisis pasar melalui:

- 🗺️ Visualisasi data peta (Geo Plot)
- 📈 Grafik interaktif
- 💡 Rekomendasi pemasaran berdasarkan wilayah
- 🤖 Chat AI berbasis LLM (Large Language Model)

Tujuan dari dashboard ini adalah membantu PT Telekomunikasi Selular Jember agar lebih cepat dan tepat dalam mengambil keputusan strategi bisnis berdasarkan kondisi pasar terkini.

---

## 🚀 Fitur Utama

- **Visualisasi Peta**: Menunjukkan persebaran pasar berdasarkan wilayah Kabupaten Jember.
- **Grafik Analitik**: Menyajikan data tren pasar secara informatif dan interaktif.
- **AI Assistant**: Membantu menjawab pertanyaan terkait data dengan dukungan LLM.
- **Rekomendasi Wilayah**: Menyediakan insight lokasi yang potensial untuk strategi pemasaran.

---

## 🛠️ Teknologi yang Digunakan

- 🐍 Python
- 🖥️ Streamlit
- 🔒 Google Authentication Platform
- 🗄️ MySQL
- 📊 Google Spreadsheet

---

## 📦 Cara Instalasi & Menjalankan

1. **Clone repositori**  
   ```bash
   git clone git clone https://github.com/SatriaBelva/TelekomunikasiSelular.git
   cd Magang\streamlit
2. **Install dependensi**  
   ```bash
   pip install streamlit
   pip install -r requirements.txt
3. **Install dependensi**  
   Buat file .streamlit/secrets.toml dan isi sesuai kredensial kamu (contoh: database, client_id, dsb)
   
4. **Jalankan aplikasi**  
   ```bash
   streamlit run main.py   

## 🔐 Autentikasi

Aplikasi ini menggunakan login via Google OAuth. Hanya email yang terdaftar dalam whitelist database yang diperbolehkan mengakses aplikasi.
---