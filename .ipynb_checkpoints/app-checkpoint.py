# app.py
import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("cicids_rf_model.pkl")
label_encoder = joblib.load("cicids_label_encoder.pkl")
feature_names = joblib.load("cicids_features.pkl")

st.title("🚨 CICIDS Intrusion Detection")
st.write("Enter feature values to detect whether traffic is normal or an attack.")

# Create dynamic inputs for all features
user_input = []
for feature in feature_names:
    value = st.number_input(f"{feature}", min_value=0.0, max_value=1e6, value=0.0)
    user_input.append(value)

input_array = np.array(user_input).reshape(1, -1)

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_array)[0]
    pred_label = label_encoder.inverse_transform([prediction])[0]
    st.success(f"🛡️ Prediction: {pred_label}")

    # Probabilities
    proba = model.predict_proba(input_array)[0]
    proba_df = pd.DataFrame({label_encoder.classes_[i]: [proba[i]] for i in range(len(proba))})
    st.bar_chart(proba_df.T)
 