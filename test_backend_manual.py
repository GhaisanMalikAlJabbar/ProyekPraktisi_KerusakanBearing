
from src.predictor import load_model, diagnose_bearing


# 1. Memuat model
print("Memuat model...")
model = load_model()
print("Model berhasil dimuat!")


# 2. Contoh input pengujian
# Nilai berikut hanya contoh untuk menguji alur backend,
# bukan hasil pengukuran mesin yang sebenarnya.
sample_input = {
    "posisi_sensor": "drive_end",
    "kecepatan_rpm": 2547.0,
    "beban_kN": 2.79,
    "suhu_housing_C": 53.8,
    "rms_g": 0.5168,
    "puncak_g": 1.1658,
    "kurtosis": 0.039,
    "crest_factor": 2.256,
    "energi_bpfo": 0.1400,
    "energi_bpfi": 0.0436,
    "energi_bsf": 0.0629,
    "frekuensi_dominan_hz": 40.9
}


# 3. Menjalankan diagnosis lengkap
print("\nMenjalankan diagnosis...")
result = diagnose_bearing(sample_input, model)


# 4. Menampilkan hasil prediksi
print("\n========== HASIL DIAGNOSIS ==========")
print("Kondisi bearing:", result["prediction"])

print("\nProbabilitas setiap kelas:")
for label, probability in result["probabilities"].items():
    print(f"- {label}: {probability * 100:.2f}%")


# 5. Menampilkan rekomendasi
recommendation = result["recommendation"]

print("\n========== REKOMENDASI ==========")
print("Status:", recommendation["status"])

print("\nTindakan:")
for item in recommendation["action"]:
    print("-", item)

print("\nPersiapan suku cadang:")
if recommendation["spare_parts"]:
    for item in recommendation["spare_parts"]:
        print("-", item)
else:
    print("Tidak ada suku cadang pengganti yang perlu disiapkan.")

print("\nInspeksi:")
for item in recommendation["inspection"]:
    print("-", item)


# 6. Pemeriksaan struktur hasil
assert result["prediction"] in [
    "normal", "bola", "inner_race", "outer_race"
]

assert abs(sum(result["probabilities"].values()) - 1.0) < 1e-5

assert result["recommendation"]["diagnosis"] == result["prediction"]

print("\n========== TEST INTEGRASI BERHASIL ==========")
