import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load model artifacts
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

app = FastAPI()

class CustomerData(BaseModel):
    data: dict

@app.post("/predict")
def predict_churn(request: CustomerData):

    df = pd.DataFrame([request.data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=feature_names, fill_value=0)
    df_scaled = scaler.transform(df)

    churn_prob = model.predict_proba(df_scaled)[0][1]

    return {
        "churn_probability": round(float(churn_prob), 3),
        "churn_prediction": "Yes" if churn_prob >= 0.5 else "No"
    }
