from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the Sentiment analysis API!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
