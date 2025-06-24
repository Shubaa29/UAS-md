from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle

app = FastAPI()

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    print("✅ Model loaded.")
except Exception as e:
    print("❌ Failed to load model:", e)

class ObesityInput(BaseModel):
    Gender: str
    Age: int
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

@app.post("/predict")
def predict(data: ObesityInput):
    try:
        input_data = data.dict()
        prediction = model.predict([input_data])
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
