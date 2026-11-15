
import pytest

from src.validation import validate_input


def test_valid_input(model, sample_input):
    result = validate_input(sample_input, model)

    assert len(result) == 12
    assert result["posisi_sensor"] == "drive_end"


def test_missing_value(model, sample_input):
    sample_input["rms_g"] = None

    with pytest.raises(ValueError):
        validate_input(sample_input, model)


def test_invalid_category(model, sample_input):
    sample_input["posisi_sensor"] = "unknown"

    with pytest.raises(ValueError):
        validate_input(sample_input, model)


def test_invalid_numeric(model, sample_input):
    sample_input["kecepatan_rpm"] = "abc"

    with pytest.raises(ValueError):
        validate_input(sample_input, model)


def test_missing_feature(model, sample_input):
    del sample_input["rms_g"]

    with pytest.raises(ValueError):
        validate_input(sample_input, model)
