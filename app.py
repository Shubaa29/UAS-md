import streamlit as st
import requests

st.title("Obesity Prediction App")

# Input Form
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1.7)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=70.0)
family_history = st.selectbox("Family History of Overweight", ["yes", "no"])
favc = st.selectbox("High Calorie Food Consumption (FAVC)", ["yes", "no"])
fcvc = st.slider("Vegetable Consumption Frequency (1.0 - 3.0)", 1.0, 3.0, 2.0)
ncp = st.slider("Number of Main Meals (1 - 4)", 1, 4, 3)
caec = st.selectbox("Food Between Meals (CAEC)", ["Never", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do You Smoke?", ["yes", "no"])
ch2o = st.slider("Daily Water Intake (1.0 - 3.0)", 1.0, 3.0, 2.0)
scc = st.selectbox("Monitor Caloric Intake (SCC)", ["yes", "no"])
faf = st.slider("Physical Activity Frequency (0.0 - 3.0)", 0.0, 3.0, 1.0)
tue = st.slider("Technology Usage (0.0 - 3.0)", 0.0, 3.0, 1.0)
calc = st.selectbox("Alcohol Consumption", ["Never", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Transportation Mode", ["Public_Transportation", "Walking", "Bike", "Motorbike", "Automobile"])

# API URL (ganti sesuai URL ngrok kamu)
API_URL = "https://a812-34-148-102-68.ngrok-free.app/predict"

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
