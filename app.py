
from flask import Flask, request, jsonify
from main import app
from joblib import load
from pandas.core.frame import DataFrame
import numpy as np
from model import model_functions
from model import data
from main import User
from main import cat_features


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_items():
    return {"message": "Hello, welcome to our app!"}

@app.route('/dan', methods=['POST'])
def inferences(user_data: User):
    model_object = load("model/model.joblib")
    encoder = load("model/encoder.joblib")
    lb = load("model/lb.joblib")

    array = np.array([[
                     user_data.age,
                     user_data.workclass,
                     user_data.education,
                     user_data.maritalStatus,
                     user_data.occupation,
                     user_data.relationship,
                     user_data.race,
                     user_data.sex,
                     user_data.hoursPerWeek,
                     user_data.nativeCountry
                     ]])

    df_temp = DataFrame(data=array, columns=[
        "age",
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "hours-per-week",
        "native-country",
    ])
    X, _, _, _ = data.process_data(
        df_temp,
        categorical_features=cat_features,
        encoder=encoder, lb=lb, training=False)
    pred = model_functions.inference(model_object, X)
    y = lb.inverse_transform(pred)[0]
    return {"prediction": y}

if __name__ == '__main__':
    app.run(debug=True)
