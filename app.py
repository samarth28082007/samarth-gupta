import streamlit as st
import pickle

# Load model
model = pickle.load(open('model/model.pkl', 'rb'))

st.title("📊 Student Marks Prediction")

hours = st.number_input("Enter study hours:")

if st.button("Predict"):
    prediction = model.predict([[hours]])
    st.success(f"Predicted Marks: {prediction[0]:.2f}")