from fastapi import FastAPI
from pydantic import BaseModel, Field
from models.load_models import load_models

PREDICTION_MAP = {0: "negative", 1: "neutral", 2: "positive"}

model_embedder, model_classifier = load_models()

app = FastAPI()


class SentimentRequest(BaseModel):
    text: str = Field(min_length=1)


class SentimentResponse(BaseModel):
    prediction: str


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the Sentiment analysis API!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/mock_predict", response_model=SentimentResponse)
def mock_predict(request: SentimentRequest) -> SentimentResponse:
    return SentimentResponse(prediction="positive")


@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest) -> SentimentResponse:
    embeddings = model_embedder.encode([request.text])
    predicted_class = int(model_classifier.predict(embeddings)[0])
    return SentimentResponse(prediction=PREDICTION_MAP[predicted_class])
