from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    sentiment: str


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the Sentiment analysis API!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: SentimentRequest) -> SentimentResponse:
    return SentimentResponse(sentiment="positive")
