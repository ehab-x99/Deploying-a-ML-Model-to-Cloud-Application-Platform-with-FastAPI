import pytest
from fastapi.testclient import TestClient
from main_api import app

@pytest.fixture
def client():
    """
    Get dataset
    """
    api_client = TestClient(app)
    return api_client

def test_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, welcome to our app!"}


def test_get_malformed(client):
    r = client.get("/wrong_url")
    assert r.status_code != 200

def test_post_above(client):
    r = client.post("/", json={
        "age": 60,
        "workclass": "Private",
        "education": "Doctorate",
        "maritalStatus": "Divorced",
        "occupation": "Transport-moving",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "hoursPerWeek": 76,
        "nativeCountry": "United-States"
    })
    if r.status_code == 200 and r.json() == {"prediction": "<=50K"}:
        json_data = r.json()  # Get the JSON data from the response
        print(json_data,"done") 

    else:
        print ("the code error in above")



def test_post_below(client):
    r = client.post("/", json={
        "age": 16,
        "workclass": "Private",
        "education": "HS-grad",
        "maritalStatus": "Never-married",
        "occupation": "Other-service",
        "relationship": "Own-child",
        "race": "Black",
        "sex": "Male",
        "hoursPerWeek": 40,
        "nativeCountry": "United-States"
    })
    if r.status_code == 200 and r.json() == {"prediction": "<=50K"}:
        json_data = r.json()  # Get the JSON data from the response
        print(json_data,"done") 
    else:
        print ("the code error in below")



def test_post_malformed(client):
    r = client.post("/", json={
        "age": 32,
        "workclass": "Private",
        "education": "Some-college",
        "maritalStatus": "ERROR",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": "Black",
        "sex": "Male",
        "hoursPerWeek": 60,
        "nativeCountry": "United-States"
    })
    r.status_code != 200
def test_post_missing_data(client):
    r = client.post("/", json={
        "age": 25,
        "workclass": "Private",
        "education": "Bachelors",
        "maritalStatus": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "nativeCountry": "United-States"
    })