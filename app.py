import streamlit as st
import pandas as pd
import cloudpickle
import requests
import os

st.set_page_config(page_title="Obesity Prediction", layout="centered")

# === Load local model sebagai fallback ===
MODEL_PATH = "model.pkl"
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        local_model = cloudpickle.load(f)
    model_loaded = True
else:
    local_model = None
    model_loaded = False

st.title("🍔 Obesity Level Predictor")
st.markdown("Prediksi tingkat obesitas berdasarkan gaya hidup dan kebiasaan sehari-hari.")

def user_input():
    col1, col2 = st.columns(2)
    with col1:
        Gender = st.selectbox("Gender", ["Male", "Female"])
        Age = st.slider("Age", 10, 100)
        Height = st.number_input("Height (m)", 1.0, 2.5, 1.7)
        Weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        family_history = st.selectbox("Family History of Overweight", ["yes", "no"])
        FAVC = st.selectbox("Frequent High Calorie Food Consumption", ["yes", "no"])
        FCVC = st.slider("Vegetable Consumption Frequency", 1.0, 3.0)
        NCP = st.slider("Number of Main Meals", 1.0, 4.0)
        CAEC = st.selectbox("Eating Between Meals", ["no", "Sometimes", "Frequently", "Always"])

    with col2:
        SMOKE = st.selectbox("Do you smoke?", ["yes", "no"])
        CH2O = st.slider("Water Intake (L)", 1.0, 3.0)
        SCC = st.selectbox("Monitor Calories", ["yes", "no"])
        FAF = st.slider("Physical Activity", 0.0, 3.0)
        TUE = st.slider("Technology Use (hours)", 0.0, 3.0)
        CALC = st.selectbox("Alcohol Consumption", ["no", "Sometimes", "Frequently", "Always"])
        MTRANS = st.selectbox("Transport", ["Walking", "Public_Transportation", "Automobile", "Motorbike", "Bike"])

    return {
        "Gender": Gender,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "family_history_with_overweight": family_history,
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

# Ambil input
input_data = user_input()

# Tombol prediksi
if st.button('🔍 Predict'):
    try:
        # GANTI URL ini sesuai dengan backend kamu
        API_URL = "https://obesity-api.onrender.com/predict"
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"🌟 Predicted Obesity Level: {result['prediction']}")
        else:
            raise Exception(f"API Error: {response.text}")

    except requests.exceptions.ConnectionError:
        st.warning("⚠️ Tidak dapat terhubung ke API, mencoba dengan model lokal...")
        if model_loaded:
            try:
                df_input = pd.DataFrame([input_data])
                pred = local_model.predict(df_input)[0]
                st.success(f"🌟 Predicted Obesity Level (Local Model): {pred}")
            except Exception as e:
                st.error(f"❌ Error saat prediksi dengan model lokal: {e}")
        else:
            st.error("❌ Model lokal tidak tersedia.")

    except Exception as e:
        st.error(f"❌ Error tidak terduga: {e}")
