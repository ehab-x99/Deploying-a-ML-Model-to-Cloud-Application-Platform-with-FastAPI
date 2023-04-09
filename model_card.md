# Model Card
This Model Card describes the Random Forest model developed by Ehab Osama to predict the income level of individuals based on a handful of attributes. The model uses default hyperparameters in scikit-learn 0.24.2.
Original paper introducing the concept of model card canbe found here: https://arxiv.org/pdf/1810.03993.pdf
## Model Details
The model was created by Ehab Osama using the Random Forest algorithm with default hyperparameters in scikit-learn 0.24.2.
## Intended Use
This model is intended to predict if individuals earn an income above or below 50,000 dollars per year based on several attributes. It is meant to be used in applications such as financial planning and budgeting.
## Training Data
The training data consisted of 80% of the original data, with the target class being the income level, which was divided into two categories: salaries over 50,000 dollars and salaries below 50,000 dollars. The training data was one-hot encoded and label-binarized to prepare it for model training.
## Evaluation Data
The evaluation data consisted of the remaining 20% of the original data, with the same attributes as the training data. It was one-hot encoded but no label-binarization was performed.
## Metrics
The model was evaluated using F1 score, precision, and recall. The precision was 0.7454, the recall was 0.615, and the F1 score was 0.6739.
## Ethical Considerations
The dataset used to train the model contains data on race and gender, which may lead to potential discrimination against individuals in certain categories. A deeper analysis of this issue may be necessary to ensure ethical use of the model.
## Caveats and Recommendations
Since some countries have much more data than others, it is recommended that more work is done to capture more data from underrepresented countries to result in a more fair and unbiased model. It is also recommended to consider incorporating additional features that may be relevant to predicting income levels, such as education level and job experience.