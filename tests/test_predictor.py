
from src.predictor import predict_bearing, diagnose_bearing


def test_model_prediction(model, sample_input):
    result = predict_bearing(model, sample_input)

    assert result["prediction"] in [
        "normal", "bola", "inner_race", "outer_race"
    ]

    assert len(result["probabilities"]) == 4


def test_probability_sum(model, sample_input):
    result = predict_bearing(model, sample_input)

    total = sum(result["probabilities"].values())

    assert abs(total - 1.0) < 1e-5


def test_complete_diagnosis(model, sample_input):
    result = diagnose_bearing(sample_input, model)

    assert "prediction" in result
    assert "probabilities" in result
    assert "recommendation" in result

    assert (
        result["recommendation"]["diagnosis"]
        == result["prediction"]
    )
