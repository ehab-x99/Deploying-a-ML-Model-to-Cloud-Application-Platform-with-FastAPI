import numpy as np
import pandas as pd
import os
import sklearn
from sklearn.model_selection import train_test_split
from starter.ml.data import process_data
from starter.ml.model import train_model, compute_model_metrics, inference
import json
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


# A function to test the get
def test_get():
    response = client.get("/welcome")
    assert response.status_code == 200
    assert response.json() == {"Hello, welcome to our app!"}


# A function to test the post on a predicted value of Salary <50K
def test_post_1():
    input_dict = {
        "age": 25,
        "workclass": "Self-emp-not-inc",
        "fnlgt": 176756,
        "education": "HS-grad",
        "education-num": 9,
        "marital-status": "Never-married",
        "occupation": "Farming-fishing",
        "relationship": "Own-child",
        "race": "White",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 35,
        "native-country": "United-States"
    }
    response = client.post("/predict", json=input_dict)
    assert response.status_code == 200
    assert response.json() == {'prediction': 'Income <= 50K'}


# A function to test the post on a predicted value of Salary>50K
def test_post_2():
    input_dict = {
        "age": 57,
        "workclass": "Federal-gov",
        "fnlgt": 337895,
        "education": "Bachelors",
        "education-num": 13,
        "marital-status": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "Black",
        "sex": "Female",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 40,
        "native-country": "United-States"
    }
    response = client.post("/predict", json=input_dict)
    assert response.status_code == 200
    assert response.json() == {'prediction': 'Income > 50K'}
# load the data.
data = pd.read_csv(os.path.join(os.getcwd(), "project-3/data/census.csv"))

# Train test split
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# Process the test data with the process_data function.
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)


def test_train_model():
    # Tests that this function returns a trained RandomForest Classifier
    model = train_model(X_train, y_train)
    assert isinstance(model, sklearn.ensemble._forest.RandomForestClassifier)
    print('Test train_model PASSED')


def test_compute_model_metrics():
    # Tests that the compute_model_metrics() function returns three metrics
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    metrics = compute_model_metrics(y_train, preds)
    assert len(metrics) == 3
    assert isinstance(metrics, tuple)
    for metric in metrics:
        assert 0 <= metric <= 1

    print('Test compute_model_metrics PASSED')


def test_inference():
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    assert len(preds) == len(X_train)  # Assert that the length is the same as x_train
    assert np.all((preds == 0) | (preds == 1)) == True  # Assert all values are 0 or 1
    print('Test inference PASSED')


if __name__ == "__main__":
    test_train_model()
    test_compute_model_metrics()
    test_inference()

    test_get()
    test_post_1()
    test_post_2()

