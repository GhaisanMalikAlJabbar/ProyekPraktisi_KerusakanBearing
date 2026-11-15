
from src.recommendation import get_recommendation


test_cases = [
    "normal",
    "bola",
    "inner_race",
    "outer_race"
]

for diagnosis in test_cases:
    print(f"\n=== TEST: {diagnosis.upper()} ===")

    result = get_recommendation(diagnosis)

    print("Status:", result["status"])
    print("Diagnosis:", result["diagnosis"])

    print("\nTindakan:")
    for item in result["action"]:
        print("-", item)

    print("\nPersiapan suku cadang:")
    if result["spare_parts"]:
        for item in result["spare_parts"]:
            print("-", item)
    else:
        print("Tidak ada suku cadang pengganti yang perlu disiapkan.")

    print("\nInspeksi:")
    for item in result["inspection"]:
        print("-", item)


print("\n=== TEST KELAS TIDAK VALID ===")

try:
    get_recommendation("unknown")
except ValueError as error:
    print("Berhasil mendeteksi error:", error)


print("\n=== TEST INPUT KOSONG ===")

try:
    get_recommendation("")
except ValueError as error:
    print("Berhasil mendeteksi error:", error)
