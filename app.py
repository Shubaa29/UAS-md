# app.py - Streamlit Frontend for Obesity Prediction

import streamlit as st
import requests

st.title("Obesity Prediction App")
st.write("Masukkan data gaya hidup untuk memprediksi tingkat obesitas.")

# Form input
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1.0, max_value=100.0)
height = st.number_input("Height (meter)", min_value=1.0, max_value=2.5)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0)
family_history = st.selectbox("Family History of Overweight", ["yes", "no"])
favc = st.selectbox("High Calorie Food Consumption (FAVC)", ["yes", "no"])
fcvc = st.slider("Vegetable Consumption Frequency (1-3)", 1.0, 3.0)
ncp = st.slider("Number of Main Meals (1-4)", 1.0, 4.0)
caec = st.selectbox("Food Between Meals (CAEC)", ["Never", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do You Smoke?", ["yes", "no"])
ch2o = st.slider("Daily Water Intake (1-3)", 1.0, 3.0)
scc = st.selectbox("Monitor Caloric Intake (SCC)", ["yes", "no"])
faf = st.slider("Physical Activity Frequency (0-3)", 0.0, 3.0)
tue = st.slider("Time Using Technology (0-3)", 0.0, 3.0)
calc = st.selectbox("Alcohol Consumption (CALC)", ["Never", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Transportation Mode", ["Public_Transportation", "Walking", "Bike", "Motorbike", "Automobile"])

# Submit to FastAPI
if st.button("Predict"):
    input_data = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history_with_overweight": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }

    # Ganti URL berikut dengan ngrok public URL-mu
    API_URL = "https://ffc9-34-148-102-68.ngrok-free.app/predict"
    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()
        st.success(f"Tingkat Obesitas: {result['prediction']}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
