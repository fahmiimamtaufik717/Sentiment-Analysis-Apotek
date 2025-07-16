import streamlit as st
import joblib

# Load model
model = joblib.load("sentiment_model.pkl")

st.set_page_config(page_title="Sentiment Analysis Apotek", page_icon="💊")

st.title("💊 Sentiment Analysis Apotek")
st.write("Masukkan review obat, lalu lihat prediksi sentimennya di bawah:")

# Input
user_input = st.text_area("📝 Review obat", "")

if st.button("🚀 Prediksi Sentiment"):
    if user_input.strip() != "":
        prediction = model.predict([user_input])[0]
        
        # Tampilkan hasil prediksi dengan warna & emoji
        if prediction == "positive":
            st.success(f"✅ Sentimen Positif 😊\n\nModel memprediksi review ini bersentimen positif.")
        elif prediction == "negative":
            st.error(f"🚫 Sentimen Negatif 😞\n\nModel memprediksi review ini bersentimen negatif.")
        else:
            st.info(f"ℹ️ Sentimen Netral 😐\n\nModel memprediksi review ini bersentimen netral.")
    else:
        st.warning("Silakan masukkan review terlebih dahulu.")
