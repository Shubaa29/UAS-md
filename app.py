with st.form("prediction_form"):
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.slider("Age", 10, 100)
    Height = st.number_input("Height (in meters)", 1.0, 2.5, 1.5)
    Weight = st.number_input("Weight (in kg)", 30.0, 200.0, 60.0)
    family_history_with_overweight = st.selectbox("Family History", ["yes", "no"])
    FAVC = st.selectbox("Frequent High Calorie Food", ["yes", "no"])
    FCVC = st.slider("Vegetable Consumption", 1.0, 3.0)
    NCP = st.slider("Number of Meals", 1.0, 4.0)
    CAEC = st.selectbox("Eating Between Meals", ["no", "Sometimes", "Frequently", "Always"])
    SMOKE = st.selectbox("Smoke", ["yes", "no"])
    CH2O = st.slider("Water Intake", 1.0, 3.0)
    SCC = st.selectbox("Monitor Calories", ["yes", "no"])
    FAF = st.slider("Physical Activity", 0.0, 3.0)
    TUE = st.slider("Tech Use", 0.0, 3.0)
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
            st.error("Key 'prediction' not found in response.")
            st.text(result)

    except Exception as e:
        st.error(f"Unexpected error: {e}")
