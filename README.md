# Air Quality Analysis Dashboard

## Deskripsi

This dashboard is designed to analyze air quality based on PM2.5 and wind speed (WSPM) data. Visualization of the relationship between wind speed and pollutant concentrations, as well as the number of days in each air quality category, such as "Good," "Moderate," to "Hazardous." This dashboard makes it easier for users to understand air quality patterns and the factors that influence them through interactive and informative graphics.

---

## Struktur Proyek

```text
submission
   Dashboard
      main.py         # Script utama untuk menjalankan dashboard menggunakan Streamlit.
      data.csv        # File data yang digunakan sebagai input untuk dashboard.
   Data
      data.csv        # Dataset mentah untuk analisis, disimpan di folder Data.
   notebook.ipynb     # Notebook Jupyter untuk eksplorasi data dan analisis awal.
   README.md          # Dokumentasi proyek ini.
   requirements.txt   # File daftar dependensi Python yang dibutuhkan.
   link.txt           # File berisi tautan sumber data dan referensi lainnya.
```

---

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan proyek:

1. Clone repositori ini ke komputer Anda:

   ```bash
   git clone https://github.com/zakyrmh/Belajar-Analisis-Data-dengan-Python.git
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd Belajar-Analisis-Data-dengan-Python
   ```

3. Instal paket Python yang dibutuhkan dengan menjalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Untuk menjalankan dashboard, ikuti langkah berikut:

1. Masuk ke folder `Dashboard`:

   ```bash
   cd Belajar-Analisis-Data-dengan-Python/Dashboard
   ```

2. Jalankan script utama menggunakan Streamlit:
   ```bash
   streamlit run main.py
   ```

---

## Data Sources

Data yang digunakan dalam proyek ini berasal dari tautan berikut:

[Air Quality Data - Google Drive](https://drive.google.com/file/d/1RhU3gJlkteaAQfyn9XOVAz7a5o1-etgr/view?usp=share_link)

---

Terima kasih telah menggunakan proyek ini! Jangan ragu untuk memberikan masukan atau membuka _issue_ pada repositori jika menemukan masalah.
