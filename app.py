# file: app.py

import streamlit as st
import joblib

# Load model
model = joblib.load('sentiment_model.pkl')

st.title("Sentiment Analysis Apotek")
st.write("Masukkan review obat, lalu lihat prediksi sentiment:")

# Input
user_input = st.text_area("Review obat", "")

if st.button("Prediksi Sentiment"):
    if user_input.strip() != "":
        prediction = model.predict([user_input])[0]
        st.write(f"**Prediksi sentiment:** {prediction}")
    else:
        st.warning("Silakan masukkan teks review terlebih dahulu.")
