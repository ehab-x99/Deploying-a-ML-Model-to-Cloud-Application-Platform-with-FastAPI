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


if __name__ == "__main__":
    test_get()
    test_post_1()
    test_post_2()
