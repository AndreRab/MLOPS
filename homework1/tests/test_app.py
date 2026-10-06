import pytest
from fastapi.testclient import TestClient

from app import PREDICTION_MAP, app
from models.load_models import load_models

client = TestClient(app)


def test_models_load_from_local_files():
    embedder, classifier = load_models()

    assert embedder is not None
    assert classifier is not None
    assert callable(embedder.encode)
    assert callable(classifier.predict)


@pytest.mark.parametrize(
    "text",
    [
        "I loved this movie; it was wonderful.",
        "The product arrived as described.",
        "This was disappointing and frustrating.",
    ],
)
def test_predict_returns_valid_json_for_sample_text(text: str):
    response = client.post("/predict", json={"text": text})

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json().keys() == {"prediction"}
    assert response.json()["prediction"] in PREDICTION_MAP.values()


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"text": ""},
        {"text": 123},
    ],
)
def test_invalid_input_returns_json_validation_error(payload: dict):
    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert response.headers["content-type"].startswith("application/json")
    body = response.json()
    assert "detail" in body
    assert body["detail"]


def test_response_model_has_prediction_string():
    response = client.post("/predict", json={"text": "A perfectly ordinary sentence."})

    assert response.status_code == 200
    prediction = response.json()["prediction"]
    assert isinstance(prediction, str)
    assert prediction in {"negative", "neutral", "positive"}
