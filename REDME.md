## Credit Card Fraud Detection 


## Overview
This project predicts whether a credit card transaction is fraudulent using Machine Learning models like Logistic Regression and Random Forest.

## How to Run

1. Download the dataset from [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud).
2. Place the `creditcard.csv` file inside the `data/` folder.
3. Run the preprocessing notebook to generate `X_train.npy`, `X_test.npy`, `y_train.npy`, and `y_test.npy`.
4. Train models using `model_training.py`.
5. Evaluate models and tune hyperparameters.

## Models Used
- Logistic Regression
- Random Forest
- GridSearchCV for hyperparameter tuning (optional)

## Note
Large files like `.csv` and `.npy` are not included in the GitHub repo due to size limitations.
