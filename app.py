
import streamlit as st
import pandas as pd

from src.predictor import load_model, diagnose_bearing


# ==========================================
# KONFIGURASI APLIKASI
# ==========================================

st.set_page_config(
    page_title="Bearing Diagnosis System",
    page_icon="⚙️",
    layout="wide"
)


# ==========================================
# MEMUAT MODEL
# ==========================================

@st.cache_resource
def get_model():
    return load_model()


# ==========================================
# HEADER
# ==========================================

st.title("⚙️ Bearing Diagnosis System")

st.write(
    "Sistem diagnosis kondisi bearing menggunakan "
    "Machine Learning berdasarkan data pengukuran getaran."
)

st.divider()


# ==========================================
# FORM INPUT
# ==========================================

st.subheader("1. Input Data Pengukuran")

st.info(
    "Masukkan 12 fitur pengukuran sesuai hasil sensor. "
    "Pastikan satuan dan metode pengukuran sesuai dengan "
    "dataset pelatihan model."
)

with st.form("bearing_input_form"):

    posisi_sensor = st.selectbox(
        "Posisi Sensor",
        options=["drive_end", "fan_end"]
    )

    col1, col2 = st.columns(2)

    with col1:
        kecepatan_rpm = st.number_input(
            "Kecepatan (RPM)", value=0.0
        )

        beban_kN = st.number_input(
            "Beban (kN)", value=0.0
        )

        suhu_housing_C = st.number_input(
            "Suhu Housing (°C)", value=0.0
        )

        rms_g = st.number_input(
            "RMS (g)", value=0.0
        )

        puncak_g = st.number_input(
            "Puncak (g)", value=0.0
        )

        kurtosis = st.number_input(
            "Kurtosis", value=0.0
        )

    with col2:
        crest_factor = st.number_input(
            "Crest Factor", value=0.0
        )

        energi_bpfo = st.number_input(
            "Energi BPFO", value=0.0
        )

        energi_bpfi = st.number_input(
            "Energi BPFI", value=0.0
        )

        energi_bsf = st.number_input(
            "Energi BSF", value=0.0
        )

        frekuensi_dominan_hz = st.number_input(
            "Frekuensi Dominan (Hz)", value=0.0
        )

    submitted = st.form_submit_button(
        "Jalankan Diagnosis",
        type="primary",
        use_container_width=True
    )


# ==========================================
# PROSES DIAGNOSIS
# ==========================================

if submitted:

    input_data = {
        "posisi_sensor": posisi_sensor,
        "kecepatan_rpm": kecepatan_rpm,
        "beban_kN": beban_kN,
        "suhu_housing_C": suhu_housing_C,
        "rms_g": rms_g,
        "puncak_g": puncak_g,
        "kurtosis": kurtosis,
        "crest_factor": crest_factor,
        "energi_bpfo": energi_bpfo,
        "energi_bpfi": energi_bpfi,
        "energi_bsf": energi_bsf,
        "frekuensi_dominan_hz": frekuensi_dominan_hz
    }

    try:
        with st.spinner("Sedang melakukan diagnosis..."):

            model = get_model()

            result = diagnose_bearing(
                input_data,
                model
            )

        # ==================================
        # HASIL DIAGNOSIS
        # ==================================

        st.divider()
        st.subheader("2. Hasil Diagnosis")

        prediction = result["prediction"]
        probabilities = result["probabilities"]

        status = result["recommendation"]["status"]

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Kondisi Bearing",
                prediction.upper()
            )

        with col2:
            confidence = probabilities[prediction] * 100

            st.metric(
                "Probabilitas Kelas Terpilih",
                f"{confidence:.2f}%"
            )

        st.info(status)

        # ==================================
        # PROBABILITAS
        # ==================================

        st.subheader("3. Probabilitas Setiap Kelas")

        probability_df = pd.DataFrame({
            "Kelas": list(probabilities.keys()),
            "Probabilitas (%)": [
                value * 100
                for value in probabilities.values()
            ]
        })

        st.bar_chart(
            probability_df.set_index("Kelas")
        )

        st.dataframe(
            probability_df,
            hide_index=True,
            use_container_width=True
        )

        # ==================================
        # REKOMENDASI
        # ==================================

        recommendation = result["recommendation"]

        st.divider()
        st.subheader("4. Rekomendasi Teknisi")

        st.markdown("**Tindakan yang disarankan:**")

        for item in recommendation["action"]:
            st.write(f"- {item}")

        st.markdown("**Persiapan suku cadang:**")

        if recommendation["spare_parts"]:
            for item in recommendation["spare_parts"]:
                st.write(f"- {item}")
        else:
            st.write(
                "Tidak ada suku cadang pengganti "
                "yang perlu disiapkan."
            )

        st.markdown("**Pemeriksaan lanjutan:**")

        for item in recommendation["inspection"]:
            st.write(f"- {item}")

        st.success("Proses diagnosis selesai.")

    except Exception as error:
        st.error(f"Diagnosis gagal: {error}")


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Bearing Diagnosis System | Machine Learning Project"
)
