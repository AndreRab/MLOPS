import joblib


def load_model(filename="model.pkl"):
    model = joblib.load(filename)
    return model


def predict(model, data):
    predictions = model.predict(data)
    return predictions
