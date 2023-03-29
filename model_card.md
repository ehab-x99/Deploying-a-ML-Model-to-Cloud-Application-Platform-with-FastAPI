# Model Card
Original paper introducing the concept of model card canbe found here: https://arxiv.org/pdf/1810.03993.pdf
## Model Details
This model is a random forest implementation using default hyperparameters in scikit-learn 0.24.2, and was implemented by Ehab Osama.
## Intended Use
The intended use of this model is to predict whether an individual earns more or less than 50,000 dollars per year based on a few attributes.
## Training Data
The training data used in this model comprised 80% of the original data. The target variable is salary, which was divided into two categories: salaries over 50K dollars and salaries below 50K dollars. The data was one-hot encoded and label binarized.
## Evaluation Data
The evaluation data used in this model comprised the remaining 20% of the original data, and had the same attributes as the training data. The data was one-hot encoded but was not label binarized.
## Metrics
The model was evaluated using F1 score, precision, and recall. The precision value was 0.7454, the recall value was 0.615, and the F1 score was 0.6739.
## Ethical Considerations
The dataset used in this model contains information on race and gender, which could lead to discrimination against individuals belonging to certain groups. Therefore, a more in-depth analysis of the data may be necessary.
## Caveats and Recommendations
Since some countries have more data than others, further work needs to be done to collect data from underrepresented countries to create a more equitable model.
