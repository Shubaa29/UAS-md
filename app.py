import streamlit as st
import requests

st.set_page_config(page_title="Obesity Classifier", layout="centered")
st.title("🏥 Obesity Level Classifier")

with st.form("obesity_form"):
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.slider("Age", 10, 100, 25)
    Height = st.number_input("Height (m)", 1.0, 2.5, 1.7)
    Weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
    family_history_with_overweight = st.selectbox("Family History with Overweight", ["yes", "no"])
    FAVC = st.selectbox("Frequent High-Calorie Food Consumption", ["yes", "no"])
    FCVC = st.slider("Vegetable Consumption Frequency", 1.0, 3.0, 2.0)
    NCP = st.slider("Main Meals per Day", 1.0, 4.0, 3.0)
    CAEC = st.selectbox("Eating Between Meals", ["no", "Sometimes", "Frequently", "Always"])
    SMOKE = st.selectbox("Do You Smoke?", ["yes", "no"])
    CH2O = st.slider("Water Intake (1–3)", 1.0, 3.0, 2.0)
    SCC = st.selectbox("Calorie Monitoring", ["yes", "no"])
    FAF = st.slider("Physical Activity Frequency", 0.0, 3.0, 1.0)
    TUE = st.slider("Technology Use", 0.0, 3.0, 1.0)
    CALC = st.selectbox("Alcohol Consumption", ["no", "Sometimes", "Frequently", "Always"])
    MTRANS = st.selectbox("Transportation", ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"])
    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
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

    api_url = "https://YOUR_NGROK_URL.ngrok-free.app/predict"  # GANTI

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()["prediction"]
            st.success(f"Predicted Obesity Level: **{result}**")
        else:
            st.error(f"API Error {response.status_code}")
            st.error(response.text)
    except Exception as e:
        st.error(f"Connection failed: {e}")
