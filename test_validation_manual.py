
from src.predictor import load_model
from src.validation import validate_input, get_allowed_categories

model = load_model()

# Menampilkan kategori yang dikenal model
print("Kategori yang tersedia:")
print(get_allowed_categories(model))

# Contoh input valid
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

# Test input valid
print("\n=== TEST 1: INPUT VALID ===")

try:
    result = validate_input(sample_input, model)
    print("Berhasil!")
    print("Jumlah fitur:", len(result))

except Exception as e:
    print("Gagal:", e)


# Test fitur kosong
print("\n=== TEST 2: INPUT KOSONG ===")

invalid_input = sample_input.copy()
invalid_input["rms_g"] = None

try:
    validate_input(invalid_input, model)
    print("Test gagal: input kosong diterima.")

except ValueError as e:
    print("Berhasil mendeteksi error:", e)


# Test kategori tidak dikenal
print("\n=== TEST 3: KATEGORI TIDAK VALID ===")

invalid_input = sample_input.copy()
invalid_input["posisi_sensor"] = "unknown"

try:
    validate_input(invalid_input, model)
    print("Test gagal: kategori tidak valid diterima.")

except ValueError as e:
    print("Berhasil mendeteksi error:", e)


# Test nilai numerik tidak valid
print("\n=== TEST 4: INPUT NUMERIK TIDAK VALID ===")

invalid_input = sample_input.copy()
invalid_input["kecepatan_rpm"] = "abc"

try:
    validate_input(invalid_input, model)
    print("Test gagal: input numerik tidak valid diterima.")

except ValueError as e:
    print("Berhasil mendeteksi error:", e)
