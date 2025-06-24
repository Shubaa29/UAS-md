import streamlit as st
import requests

st.title("Obesity Prediction App")

# Input Form
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 1, 100)
height = st.number_input("Height (m)", 1.0, 2.5)
weight = st.number_input("Weight (kg)", 10.0, 300.0)
family_history = st.selectbox("Family History of Overweight", ["yes", "no"])
favc = st.selectbox("High Calorie Food Consumption (FAVC)", ["yes", "no"])
fcvc = st.slider("Vegetable Consumption Frequency (1-3)", 1, 3)
ncp = st.slider("Number of Main Meals (1-4)", 1, 4)
caec = st.selectbox("Food Between Meals (CAEC)", ["Never", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do You Smoke?", ["yes", "no"])
ch2o = st.slider("Daily Water Intake (1-3)", 1, 3)
scc = st.selectbox("Monitor Caloric Intake (SCC)", ["yes", "no"])
faf = st.slider("Physical Activity Frequency (0-3)", 0, 3)
tue = st.slider("Technology Usage (0-3)", 0, 3)
calc = st.selectbox("Alcohol Consumption", ["Never", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Transportation Mode", ["Public_Transportation", "Walking", "Bike", "Motorbike", "Automobile"])

# API URL (ganti sesuai URL ngrok kamu)
API_URL = "https://e6b9-34-148-102-68.ngrok-free.app/predict"

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

    try:
        response = requests.post(API_URL, json=input_data)
        st.write("Status Code:", response.status_code)
        st.write("Response:", response.text)
        if response.status_code == 200:
            result = response.json()
            if "prediction" in result:
                st.success(f"Tingkat Obesitas: {result['prediction']}")
            else:
                st.error(f"API error: {result.get('error', 'Unknown error')}")
        else:
            st.error("Server error: check backend logs.")
    except Exception as e:
        st.error(f"Gagal koneksi ke API: {e}")
