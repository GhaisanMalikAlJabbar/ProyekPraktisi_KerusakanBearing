
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

from src.predictor import load_model, diagnose_bearing


# ==========================================
# 1. INISIALISASI FASTAPI
# ==========================================

app = FastAPI(
    title="Bearing Fault Diagnosis API",
    description=(
        "REST API untuk diagnosis kerusakan bearing "
        "menggunakan Machine Learning."
    ),
    version="1.0.0"
)


# ==========================================
# 2. MEMUAT MODEL
# ==========================================

try:
    model = load_model()
    print("Model berhasil dimuat!")

except Exception as e:
    model = None
    print(f"Gagal memuat model: {e}")


# ==========================================
# 3. SKEMA INPUT
# ==========================================

class BearingInput(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        allow_inf_nan=False
    )

    posisi_sensor: Literal["drive_end", "fan_end"]

    kecepatan_rpm: float = Field(ge=0)
    beban_kN: float = Field(ge=0)
    suhu_housing_C: float

    rms_g: float = Field(ge=0)
    puncak_g: float = Field(ge=0)
    kurtosis: float
    crest_factor: float = Field(ge=0)

    energi_bpfo: float = Field(ge=0)
    energi_bpfi: float = Field(ge=0)
    energi_bsf: float = Field(ge=0)

    frekuensi_dominan_hz: float = Field(ge=0)


# ==========================================
# 4. ENDPOINT ROOT
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Bearing Fault Diagnosis API",
        "status": "running",
        "documentation": "/docs"
    }


# ==========================================
# 5. ENDPOINT HEALTH CHECK
# ==========================================

@app.get("/health")
def health_check():

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model belum berhasil dimuat."
        )

    return {
        "status": "healthy",
        "model": "loaded"
    }


# ==========================================
# 6. ENDPOINT PREDICTION
# ==========================================

@app.post("/predict")
def predict_bearing_api(data: BearingInput):

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model tidak tersedia."
        )

    try:

        input_data = data.model_dump()

        result = diagnose_bearing(
            input_data,
            model
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=422,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Kesalahan prediksi: {str(e)}"
        )


# ==========================================
# 7. ENDPOINT INFORMASI MODEL
# ==========================================

@app.get("/model-info")
def model_info():

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model tidak tersedia."
        )

    return {
        "model_type": type(
            model.named_steps["classifier"]
        ).__name__,

        "features": list(
            model.named_steps[
                "preprocessor"
            ].feature_names_in_
        ),

        "classes": [
            str(label)
            for label in model.named_steps[
                "classifier"
            ].classes_
        ]
    }
