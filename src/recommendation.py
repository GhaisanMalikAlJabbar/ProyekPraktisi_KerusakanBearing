
RECOMMENDATIONS = {
    "normal": {
        "status": "Tidak terindikasi kerusakan",
        "action": [
            "Bearing dapat tetap digunakan.",
            "Lanjutkan pemantauan kondisi getaran secara berkala.",
            "Periksa pelumasan dan kondisi operasi sesuai jadwal perawatan."
        ],
        "spare_parts": [],
        "inspection": [
            "Periksa kondisi pelumasan.",
            "Periksa temperatur dan suara operasi.",
            "Dokumentasikan hasil pengukuran sebagai data pemantauan."
        ]
    },
    "bola": {
        "status": "Terindikasi kerusakan pada elemen bola",
        "action": [
            "Lakukan inspeksi kondisi elemen gelinding.",
            "Evaluasi tingkat kerusakan sebelum menentukan penggantian bearing.",
            "Jika kerusakan terkonfirmasi, siapkan bearing pengganti dengan spesifikasi yang sesuai."
        ],
        "spare_parts": [
            "Bearing pengganti sesuai spesifikasi mesin (jika diperlukan)",
            "Pelumas bearing sesuai rekomendasi pabrikan"
        ],
        "inspection": [
            "Periksa elemen bola dan cage.",
            "Periksa kondisi lintasan gelinding.",
            "Periksa kontaminasi dan kecukupan pelumas."
        ]
    },
    "inner_race": {
        "status": "Terindikasi kerusakan pada lintasan dalam",
        "action": [
            "Lakukan inspeksi pada lintasan dalam bearing.",
            "Periksa kondisi poros dan dudukan bearing.",
            "Siapkan bearing pengganti dengan spesifikasi yang sesuai apabila kerusakan terkonfirmasi."
        ],
        "spare_parts": [
            "Bearing pengganti sesuai spesifikasi mesin",
            "Pelumas bearing sesuai rekomendasi pabrikan"
        ],
        "inspection": [
            "Periksa permukaan lintasan dalam.",
            "Periksa kondisi poros dan toleransi pemasangan.",
            "Periksa tanda keausan, retak, atau kerusakan permukaan."
        ]
    },
    "outer_race": {
        "status": "Terindikasi kerusakan pada lintasan luar",
        "action": [
            "Lakukan inspeksi pada lintasan luar bearing.",
            "Periksa kondisi housing dan dudukan bearing.",
            "Siapkan bearing pengganti dengan spesifikasi yang sesuai apabila kerusakan terkonfirmasi."
        ],
        "spare_parts": [
            "Bearing pengganti sesuai spesifikasi mesin",
            "Pelumas bearing sesuai rekomendasi pabrikan"
        ],
        "inspection": [
            "Periksa permukaan lintasan luar.",
            "Periksa kondisi housing dan dudukan bearing.",
            "Periksa tanda keausan, retak, atau kerusakan permukaan."
        ]
    }
}


def get_recommendation(prediction):
    """
    Menghasilkan rekomendasi berdasarkan kelas hasil diagnosis model.
    """
    if not isinstance(prediction, str):
        raise TypeError("Hasil diagnosis harus berupa string.")

    prediction = prediction.strip().lower()

    if not prediction:
        raise ValueError("Hasil diagnosis tidak boleh kosong.")

    if prediction not in RECOMMENDATIONS:
        raise ValueError(
            f"Kelas diagnosis '{prediction}' tidak dikenal. "
            f"Kelas yang tersedia: {list(RECOMMENDATIONS.keys())}"
        )

    result = RECOMMENDATIONS[prediction].copy()

    # Salin list agar perubahan pada hasil tidak mengubah data rekomendasi utama.
    result["action"] = list(result["action"])
    result["spare_parts"] = list(result["spare_parts"])
    result["inspection"] = list(result["inspection"])

    result["diagnosis"] = prediction

    return result
