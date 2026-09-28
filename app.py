import streamlit as st
import numpy as np
import pickle

scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('ridgecv.pkl', 'rb'))

st.set_page_config(page_title="Forest Fire Prediction", layout="centered")
st.title("Algerian Forest Fire FWI Predictor")
st.write("Enter the weather and fire indices to predict the Fire Weather Index (FWI).")

temperature = st.number_input("Temperature (°C)", value=29.0)
rh = st.number_input("Relative Humidity (RH %)", value=57.0)
ws = st.number_input("Wind Speed (Ws km/h)", value=18.0)
rain = st.number_input("Rain (mm)", value=0.0)
ffmc = st.number_input("Fine Fuel Moisture Code (FFMC)", value=65.7)
dmc = st.number_input("Duff Moisture Code (DMC)", value=3.4)
isi = st.number_input("Initial Spread Index (ISI)", value=1.3)
classes = st.selectbox("Classes", options=[0, 1], format_func=lambda x: "Fire (1)" if x == 1 else "Not Fire (0)")
region = st.selectbox("Region", options=[0, 1], format_func=lambda x: "Sidi-Bel Abbes (1)" if x == 1 else "Bejaia (0)")

if st.button("Predict FWI"):
    input_data = np.array([[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    st.subheader(f"Predicted Fire Weather Index (FWI): {prediction[0]:.2f}")