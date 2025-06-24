# main.py - FastAPI Backend for Obesity Prediction (Debugging Enhanced)

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# Load model, scaler, label encoders, and target encoder
with open("best_model.pkl", "rb") as f:
    try:
        model, scaler, label_encoders, target_encoder = pickle.load(f)
    except ValueError:
        model, scaler = pickle.load(f)
        label_encoders = None
        target_encoder = None

class ObesityInput(BaseModel):
    Gender: str
    Age: float
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Obesity Prediction API is running"}

@app.post("/predict")
def predict(data: ObesityInput):
    try:
        input_data = data.dict()
        print("📥 Input received:", input_data)

        # Encode categorical features
        if label_encoders:
            for col in label_encoders:
                input_data[col] = label_encoders[col].transform([input_data[col]])[0]
        else:
            print("⚠️ Label encoders not available")

        # Arrange input in correct order
        ordered = [
            input_data["Gender"],
            input_data["Age"],
            input_data["Height"],
            input_data["Weight"],
            input_data["family_history_with_overweight"],
            input_data["FAVC"],
            input_data["FCVC"],
            input_data["NCP"],
            input_data["CAEC"],
            input_data["SMOKE"],
            input_data["CH2O"],
            input_data["SCC"],
            input_data["FAF"],
            input_data["TUE"],
            input_data["CALC"],
            input_data["MTRANS"]
        ]

        numeric_indices = [1, 2, 3, 6, 7, 10, 12, 13]
        for i in numeric_indices:
            ordered[i] = float(ordered[i])

        scaled_input = scaler.transform([ordered])
        pred = model.predict(scaled_input)[0]

        if target_encoder:
            label = target_encoder.inverse_transform([pred])[0]
        else:
            label = int(pred)

        print("✅ Prediction:", label)
        return {"prediction": label}

    except Exception as e:
        print("❌ Error occurred:", str(e))
        return {"error": str(e)}
