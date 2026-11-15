
import pytest

from src.predictor import load_model


@pytest.fixture(scope="session")
def model():
    return load_model()


@pytest.fixture
def sample_input():
    return {
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
