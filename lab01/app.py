from fastapi import FastAPI

from api.models.iris import PredictRequest, PredictResponse
from training import load_data, train_model, save_model
from inference import load_model


app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/train")
def train_and_save_model():
    trained_model = train_model()
    save_model(trained_model)


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    model = load_model()

    features = [
        [
            request.sepal_length,
            request.sepal_width,
            request.petal_length,
            request.petal_width,
        ]
    ]

    class_id = int(model.predict(features)[0])
    species = load_data().target_names[class_id]

    return PredictResponse(prediction=species)
