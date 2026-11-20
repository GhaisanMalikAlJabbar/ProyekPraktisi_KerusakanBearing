# Proyek Praktisi Diagnosis Bearing · Tim Lorem Ipsum

**Kasus:** 4 Diagnosis Bearing · **Aplikasi:** [tautan aplikasi](https://proyekpraktisikerusakanbearing-drwvxutgx7jgafczueygac.streamlit.app/) · **Video:** [tautan video]

| Anggota | NIM | Bagian yang dikerjakan |
|---|---|---|
| Mehtar Raditya Daniswara Susanto | 2400744 | Membuat Aplikasi |
| Ghaisan Malik Aljabbar | 2400333 | [Membuat Model] |

## Masalah dan pengguna

Pengguna utama model ini adalah teknisi pemeliharaan mesin, operator industri, dan praktisi bidang mekatronika yang bertanggung jawab memantau kondisi bearing pada mesin berputar. Model Machine Learning ini membantu pengguna mengidentifikasi kondisi bearing, baik normal maupun mengalami kerusakan pada outer race, inner race, atau elemen bola, berdasarkan karakteristik data sensor dan parameter operasional. Hasil diagnosis dapat digunakan sebagai dasar pengambilan keputusan dalam menentukan kebutuhan inspeksi dan tindakan pemeliharaan mesin.

## Data dan pembersihan

| Masalah yang ditemukan | Jumlah baris | Cara menangani |
| Missing Values | 609 | Menggunakan df.isnull() |
| Duplicates | 220 | Menggunakan drop_duplicates |

## Hasil

| Model | [metrik utama] *validation* | [metrik utama] *test* |
|---|---|---|
| *Baseline*: [nama *baseline*] | | |
| [model final] | | |

*Threshold* yang dipakai: [angka], karena [alasan bisnis].

## Cara menjalankan

```bash
pip install -r requirements.txt
uvicorn app.api.main:app --reload       # API
streamlit run app/ui/streamlit_app.py   # aplikasi
```

## Struktur repositori

```
notebooks/      notebook dari EDA sampai penyimpanan model
data/           data mentah (dan data bersih jika perlu)
src/features.py fungsi pembuat fitur, dipakai saat pelatihan dan saat prediksi
artifacts/      model.joblib + metadata.json
app/            API (FastAPI) dan antarmuka (Streamlit)
```

## Keterbatasan

[Dalam kondisi apa model ini tidak dapat dipercaya? Data apa yang belum tersedia?]

## Daftar periksa sebelum dikumpulkan

- [ ] Repositori bersifat publik dan setiap anggota memiliki *commit*
- [ ] *Notebook* dapat dijalankan ulang dari awal sampai akhir tanpa galat
- [ ] *Baseline* wajib dilaporkan dan dibandingkan
- [ ] Data *test* hanya dibuka satu kali, di akhir
- [ ] `artifacts/metadata.json` berisi versi model, fitur masukan, *threshold*, dan metrik
- [ ] Aplikasi dapat dibuka orang lain melalui tautan, termasuk dari ponsel
- [ ] Aplikasi tidak berhenti mendadak ketika menerima masukan yang tidak wajar
- [ ] Laporan paling banyak 6 halaman dan video paling lama 5 menit
