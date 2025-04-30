import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models//random_forest_model.pkl")  # or logistic_regression_model.pkl

# App title
st.title("Credit Card Fraud Detection App")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file with transaction data", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:")
    st.dataframe(data.head())

    if st.button("Predict Fraud"):
        # Assuming data is already preprocessed like your training data
        predictions = model.predict(data)
        data['Prediction'] = ['Fraud' if p == 1 else 'Not Fraud' for p in predictions]
        st.write("Prediction Results:")
        st.dataframe(data)
        fraud_count = sum(predictions)
        st.success(f"Detected {fraud_count} fraudulent transactions.")

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
