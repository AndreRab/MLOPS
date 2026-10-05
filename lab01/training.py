import sklearn
import joblib


def load_data():
    iris = sklearn.datasets.load_iris()
    return iris


def train_model():
    model = sklearn.linear_model.LogisticRegression(max_iter=200)
    iris = load_data()
    model.fit(iris.data, iris.target)
    return model


def save_model(model, filename="model.pkl"):
    joblib.dump(model, filename)
