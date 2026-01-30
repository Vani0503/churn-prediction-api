# churn-prediction-api
data set source: https://www.kaggle.com/code/bandiatindra/telecom-churn-prediction
cleaned datafile after removing unused columns: cleaned_telco_churn 
Columns removed: Customer_ID
Trained ML model file: churn_model.pkl
Model evaluation:
- Accuracy: 73% (out of all the predictions, 73% predictions are correct whether users will churn or not)
- Recall: 79% (out of all the users who intend to churn, the model correctly identifed 79% of them)
- Precision: 49% (out of all predictions where the model said that the user would churn out, 49% were correct)
- At 0.5% threshold, this model has optimised results on recall, which is to identify as many churn users as possible as it is difficult to win back churned out users)
