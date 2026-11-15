
# Bearing Diagnosis System

Aplikasi diagnosis kondisi bearing berbasis Machine Learning
menggunakan data pengukuran getaran.

## Fitur

- Input 12 fitur pengukuran bearing.
- Prediksi empat kondisi bearing:
  - Normal
  - Bola
  - Inner Race
  - Outer Race
- Menampilkan probabilitas prediksi.
- Memberikan rekomendasi inspeksi dan persiapan suku cadang.

## Teknologi

- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Joblib

## Menjalankan Aplikasi Secara Lokal

1. Clone repository:

   git clone URL_REPOSITORY

2. Masuk ke direktori proyek:

   cd ProyekPraktisi_KerusakanBearing

3. Buat virtual environment:

   python -m venv .venv

4. Aktifkan virtual environment (Windows):

   .venv\Scripts\activate

5. Instal dependensi:

   pip install -r requirements.txt

6. Jalankan aplikasi:

   streamlit run app.py

## Struktur Proyek

- app.py: antarmuka aplikasi Streamlit.
- src/: backend diagnosis.
- artifacts/: model dan metadata.
- tests/: pengujian otomatis.

## Model

Model menggunakan pipeline Scikit-learn yang mencakup
preprocessing dan klasifikasi kondisi bearing.
