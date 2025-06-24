

# app.py
import streamlit as st
import requests

st.title("Obesity Level Predictor")

with st.form("prediction_form"):
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.slider("Age", 10, 100)
    Height = st.number_input("Height (in meters)", 1.0, 2.5, 1.5)
    Weight = st.number_input("Weight (in kg)", 30.0, 200.0, 60.0)
    family_history_with_overweight = st.selectbox("Family History of Overweight", ["yes", "no"])
    FAVC = st.selectbox("Frequent High Calorie Food Consumption", ["yes", "no"])
    FCVC = st.slider("Vegetable Consumption Frequency", 1.0, 3.0)
    NCP = st.slider("Number of Main Meals", 1.0, 4.0)
    CAEC = st.selectbox("Eating Between Meals", ["no", "Sometimes", "Frequently", "Always"])
    SMOKE = st.selectbox("Do you smoke?", ["yes", "no"])
    CH2O = st.slider("Water Intake (L)", 1.0, 3.0)
    SCC = st.selectbox("Monitor Calories", ["yes", "no"])
    FAF = st.slider("Physical Activity Frequency", 0.0, 3.0)
    TUE = st.slider("Technology Use (hours)", 0.0, 3.0)
    CALC = st.selectbox("Alcohol Consumption", ["no", "Sometimes", "Frequently", "Always"])
    MTRANS = st.selectbox("Transportation Mode", ["Walking", "Public_Transportation", "Automobile", "Motorbike", "Bike"])

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = {
        "Gender": Gender,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": FAVC,
        "FCVC": FCVC,
        "NCP": NCP,
        "CAEC": CAEC,
        "SMOKE": SMOKE,
        "CH2O": CH2O,
        "SCC": SCC,
        "FAF": FAF,
        "TUE": TUE,
        "CALC": CALC,
        "MTRANS": MTRANS
    }

    response = requests.post("https://obesity-api.onrender.com/predict", json=input_data)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Predicted Obesity Level: {prediction}")
    else:
        st.error("Prediction failed.")
