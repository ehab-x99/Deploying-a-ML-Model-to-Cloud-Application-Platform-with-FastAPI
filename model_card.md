# Model Card
Original paper introducing the concept of model card canbe found here: https://arxiv.org/pdf/1810.03993.pdf
## Model Details
This particular Model Card is for a Random Forest model created by Ehab Osama, using the default hyperparameters in scikit-learn 0.24.2.
## Intended Use
The Random Forest model is designed to predict whether individuals earn an income above or below 50K dollars per year, based on a set of input attributes. The model was created using scikit-learn 0.24.2, with default hyperparameters.
## Training Data
The model was trained using data from the census dataset. The training data comprised 80% of the original data, and the target class was the salary, which was divided into two categories: salaries over 50K dollars and salaries below 50K dollars. The training data was one-hot encoded and label binarized to prepare it for training.
## Evaluation Data
The model was evaluated using the remaining 20% of the original dataset, which was also one-hot encoded, but no label binarization was done.
## Metrics
The model's performance was evaluated using F1 score, precision, and recall. The precision was 0.7454, recall was 0.615, and the F1 score was 0.6739.
## Ethical Considerations
The dataset used in training the model contains data on race and gender, which could potentially lead to discrimination against individuals in these categories. To mitigate this risk, further investigation is recommended to ensure that the model does not discriminate against any particular group.
## Caveats and Recommendations
The model was trained on data that may not represent all demographic groups equally. Therefore, additional work needs to be done to ensure that the model is fair and unbiased across all demographic groups. Specifically, more data needs to be gathered from underrepresented countries to ensure that the model performs well across all regions.