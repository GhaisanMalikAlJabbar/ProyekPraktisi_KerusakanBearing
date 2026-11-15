
from pathlib import Path

import joblib
import pandas as pd

from src.validation import validate_input
from src.recommendation import get_recommendation


ROOT_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT_DIR / "artifacts" / "bearing_diagnosis_model.joblib"


def load_model():
    """Memuat model machine learning yang sudah dilatih."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"File model tidak ditemukan: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


def get_input_features(model):
    """Mengambil daftar fitur berdasarkan pipeline model."""
    preprocessor = model.named_steps["preprocessor"]
    return list(preprocessor.feature_names_in_)


def predict_bearing(model, input_data):
    """Melakukan validasi input dan prediksi kondisi bearing."""
    validated_input = validate_input(input_data, model)
    expected_features = get_input_features(model)

    input_df = pd.DataFrame(
        [[validated_input[feature] for feature in expected_features]],
        columns=expected_features
    )

    prediction = model.predict(input_df)[0]

    if not hasattr(model, "predict_proba"):
        raise RuntimeError(
            "Model tidak mendukung predict_proba()."
        )

    probabilities = model.predict_proba(input_df)[0]
    classes = model.named_steps["classifier"].classes_

    probability_result = {
        str(label): float(probability)
        for label, probability in zip(classes, probabilities)
    }

    return {
        "prediction": str(prediction),
        "probabilities": probability_result
    }


def diagnose_bearing(input_data, model):
    """
    Alur lengkap:
    validasi -> prediksi -> rekomendasi.
    """
    prediction_result = predict_bearing(model, input_data)

    recommendation = get_recommendation(
        prediction_result["prediction"]
    )

    return {
        "prediction": prediction_result["prediction"],
        "probabilities": prediction_result["probabilities"],
        "recommendation": recommendation
    }
