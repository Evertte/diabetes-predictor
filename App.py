import streamlit as st
import pandas as pd
import joblib

import urllib.request
import os

# Download model from Google Drive if not present
if not os.path.exists("Diabetes_prediction.pkl"):
    url = "https://drive.google.com/uc?export=download&id=17BkcH_4_9MAY4O1WuxqOK5x4TVbh"
    urllib.request.urlretrieve(url, "Diabetes_prediction.pkl")

# Load the trained model

model = joblib.load('Diabetes_prediction.pkl')
scaler = joblib.load("scaler.pkl")

st.title("Diabetes Prediction App 💉")
st.markdown("Fill in the details below to check the likelihood of diabetes.")

# User input form
with st.form("diabetes_form"):
    gender = st.selectbox("Gender", options=["Female", "Male"])
    age = st.slider("Age", 0, 120, 25)
    hypertension = st.selectbox("Hypertension", options=["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease", options=["No", "Yes"])
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1)
    hba1c_level = st.number_input("HbA1c Level", min_value=3.0, max_value=15.0, step=0.1)
    blood_glucose_level = st.number_input("Blood Glucose Level", min_value=50, max_value=300, step=1)
    smoking_history = st.selectbox("Smoking History", options=["never", "former", "ever", "current", "not current"])

    submitted = st.form_submit_button("Predict")

# Make prediction
if submitted:
    # Convert categorical to numerical
    gender = 1 if gender == "Male" else 0
    hypertension = 1 if hypertension == "Yes" else 0
    heart_disease = 1 if heart_disease == "Yes" else 0

    # One-hot encode smoking history
    smoking_options = {
        "smoking_history_current": 0,
        "smoking_history_ever": 0,
        "smoking_history_former": 0,
        "smoking_history_never": 0,
        "smoking_history_not current": 0
    }

    key = f"smoking_history_{smoking_history}"
    if key in smoking_options:
        smoking_options[key] = 1

    # Final input dictionary
    input_data = {
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "bmi": bmi,
        "HbA1c_level": hba1c_level,
        "blood_glucose_level": blood_glucose_level,
        **smoking_options
    }

    input_df = pd.DataFrame([input_data])
    

    # Prediction
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    # Result display
    if prediction == 1:
        st.error("⚠️ High risk of diabetes detected.")
    else:
        st.success("✅ No diabetes detected.")
