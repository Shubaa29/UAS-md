import streamlit as st
import requests

def main():
    st.title("Obesity Level Predictor")

    with st.form("prediction_form"):
        Gender = st.selectbox("Gender", ["Male", "Female"])
        Age = st.slider("Age", 10, 100)
        Height = st.number_input("Height (m)", 1.0, 2.5, 1.5)
        Weight = st.number_input("Weight (kg)", 30.0, 200.0, 60.0)
        family_history_with_overweight = st.selectbox("Family History", ["yes", "no"])
        FAVC = st.selectbox("High Calorie Food", ["yes", "no"])
        FCVC = st.slider("Vegetable Frequency", 1.0, 3.0)
        NCP = st.slider("Meals per Day", 1.0, 4.0)
        CAEC = st.selectbox("Snacking", ["no", "Sometimes", "Frequently", "Always"])
        SMOKE = st.selectbox("Smoke", ["yes", "no"])
        CH2O = st.slider("Water Intake", 1.0, 3.0)
        SCC = st.selectbox("Calorie Monitor", ["yes", "no"])
        FAF = st.slider("Physical Activity", 0.0, 3.0)
        TUE = st.slider("Tech Usage", 0.0, 3.0)
        CALC = st.selectbox("Alcohol", ["no", "Sometimes", "Frequently", "Always"])
        MTRANS = st.selectbox("Transport", ["Walking", "Public_Transportation", "Automobile", "Motorbike", "Bike"])

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

        try:
            response = requests.post("http://localhost:8000/predict", json=input_data)
            response.raise_for_status()
            result = response.json()

            if "prediction" in result:
                st.success(f"Predicted Obesity Level: {result['prediction']}")
            else:
                st.error("Key 'prediction' not found.")
                st.text(result)

        except Exception as e:
            st.error(f"Unexpected error: {e}")

# ✅ Panggil fungsi utama
if __name__ == "__main__":
    main()
