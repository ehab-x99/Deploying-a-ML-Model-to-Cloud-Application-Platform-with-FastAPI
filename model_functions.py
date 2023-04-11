# from sklearn.metrics import fbeta_score, precision_score, recall_score
# import logging
# from sklearn.ensemble import RandomForestClassifier
# from imblearn.over_sampling import SMOTE


# # Optional: implement hyperparameter tuning.
# def train_model(X_train, y_train):
#     """
#     Trains a machine learning model and returns it.

#     Inputs
#     ------
#     X_train : np.array
#         Training data.
#     y_train : np.array
#         Labels.
#     Returns
#     -------
#     model
#         Trained machine learning model.
#     """
#     try:
#         model = RandomForestClassifier()
#         smote = SMOTE(random_state=0)
#         X_train, y_train = smote.fit_resample(X_train, y_train)
#         model.fit(X_train, y_train)
#         logging.info('SUCCESS!:Model trained and saved')
#         return model
#     except BaseException:
#         logging.info('ERROR!:Model not trained and not saved')


# def model_predictions(X_test, model):
#     try:
#         predictions = model.predict(X_test)
#         logging.info('SUCCESS!:Model predictions generated')
#         return predictions
#     except BaseException:
#         logging.info('ERROR!:Model predictions not generated')


# def compute_model_metrics(y, preds):
#     """
#     Validates the trained machine learning model
#     using precision, recall, and F1.
#     Inputs
#     ------
#     y : np.array
#         Known labels, binarized.
#     preds : np.array
#         Predicted labels, binarized.
#     Returns
#     -------
#     precision : float
#     recall : float
#     fbeta : float
#     """
#     try:
#         fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
#         precision = precision_score(y, preds, zero_division=1)
#         recall = recall_score(y, preds, zero_division=1)
#         logging.info('SUCCESS: Model scoring completed')
#         return precision, recall, fbeta
#     except BaseException:
#         logging.info('ERROR: Error occurred when scoring Models')


# def inference(model, X):
#     """ Run model inferences and return the predictions.

#     Inputs
#     ------
#     model : ???
#         Trained machine learning model.
#     X : np.array
#         Data used for prediction.
#     Returns
#     -------
#     preds : np.array
#         Predictions from the model.
#     """
#     preds = model.predict(X)
#     return preds

import numpy as np
import unittest

class TestMLPipeline(unittest.TestCase):
    
    def setUp(self):
        self.X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        self.y_train = np.array([0, 0, 1, 1])
        self.X_test = np.array([[13, 14, 15], [16, 17, 18]])
        self.model = train_model(self.X_train, self.y_train)
    
    def test_train_model(self):
        self.assertIsNotNone(self.model)
    
    def test_model_predictions(self):
        predictions = model_predictions(self.X_test, self.model)
        self.assertEqual(predictions.shape[0], self.X_test.shape[0])
    
    def test_compute_model_metrics(self):
        y = np.array([0, 1])
        preds = np.array([0, 0])
        precision, recall, fbeta = compute_model_metrics(y, preds)
        self.assertEqual(precision, 0.0)
        self.assertEqual(recall, 0.0)
        self.assertEqual(fbeta, 0.0)
    
    def test_inference(self):
        preds = inference(self.model, self.X_test)
        self.assertEqual(preds.shape[0], self.X_test.shape[0])
    
if __name__ == '__main__':
    unittest.main()
