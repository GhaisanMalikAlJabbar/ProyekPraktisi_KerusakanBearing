
from src.predictor import load_model, predict_bearing

# Memuat model
model = load_model()

# Contoh input dari rekaman dataset
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

# Menjalankan prediksi
result = predict_bearing(model, sample_input)

# Menampilkan hasil
print("=== HASIL DIAGNOSIS BEARING ===")

print("\nPrediksi kondisi:")
print(result["prediction"])

print("\nProbabilitas setiap kelas:")

for kelas, probabilitas in result["probabilities"].items():
    print(f"{kelas}: {probabilitas * 100:.2f}%")

print(
    "\nTotal probabilitas:",
    sum(result["probabilities"].values()) * 100,
    "%"
)
