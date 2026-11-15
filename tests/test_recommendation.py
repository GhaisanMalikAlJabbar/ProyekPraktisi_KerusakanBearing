
import pytest

from src.recommendation import get_recommendation


@pytest.mark.parametrize(
    "diagnosis",
    ["normal", "bola", "inner_race", "outer_race"]
)
def test_valid_recommendation(diagnosis):
    result = get_recommendation(diagnosis)

    assert result["diagnosis"] == diagnosis
    assert "status" in result
    assert "action" in result
    assert "spare_parts" in result
    assert "inspection" in result


def test_normal_no_spare_parts():
    result = get_recommendation("normal")

    assert result["spare_parts"] == []


def test_invalid_diagnosis():
    with pytest.raises(ValueError):
        get_recommendation("unknown")


def test_empty_diagnosis():
    with pytest.raises(ValueError):
        get_recommendation("")
