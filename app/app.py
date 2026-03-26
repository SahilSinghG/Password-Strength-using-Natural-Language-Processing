import streamlit as st
import pickle

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

st.title("🔐 Password Strength Predictor")

password = st.text_input("Enter Password")

if st.button("Check Strength"):

    data = vectorizer.transform([password])

    prediction = model.predict(data)[0]

    labels = {
        0: "Weak",
        1: "Medium",
        2: "Strong"
    }

    st.success(f"Password Strength: {labels[prediction]}")