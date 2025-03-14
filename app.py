import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model pipeline
with open('model_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

model = pipeline['model']
pca = pipeline['pca']
scaler_minmax = pipeline['scaler']  # MinMaxScaler for PCA-transformed data

st.title("🌽 Vomitoxin Prediction in Corn")

# File uploader for CSV/Excel
uploaded_file = st.file_uploader("Upload CSV/Excel file with 448 spectral bands", type=["csv", "xlsx"])

# Manual input for comma-separated values
input_features = st.text_area("OR Enter 448 spectral values separated by commas:")

def preprocess_and_predict(data):
    """ PCA → MinMax Scaling → Prediction."""
    data_pca = pca.transform(df)  # PCA transformation
    data_normalized = scaler_minmax.transform(data_pca)  # Second scaling step

    return model.predict(data_normalized)

if uploaded_file:
    try:
        # Read the uploaded file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Ensure only 448 spectral bands are selected
        if df.shape[1] > 448:
            df = df.iloc[:, -448:]  # Keep only last 448 columns if extra ones exist

        if df.shape[1] != 448:
            st.error(f"Uploaded file must have exactly 448 spectral bands. Found {df.shape[1]} columns.")
        else:
            predictions = preprocess_and_predict(df)
            df["Predicted Vomitoxin (ppb)"] = predictions
            st.write("## Predictions:")
            st.write(df)

            # Download button for results
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Predictions as CSV", csv, "vomitoxin_predictions.csv", "text/csv")

    except Exception as e:
        st.error(f"Error processing file: {e}")

elif input_features:
    try:
        # Convert input to numpy array
        features = np.array(list(map(float, input_features.split(',')))).reshape(1, -1)

        if features.shape[1] != 448:
            st.error(f"Expected 448 values, but received {features.shape[1]}.")
        else:
            prediction = preprocess_and_predict(features)
            st.write(f"**Predicted Vomitoxin (ppb): {prediction[0]:.2f}**")

    except ValueError:
        st.error("⚠️ Please enter valid numerical values.")

st.write("🚀 **Upload a file or enter spectral values for vomitoxin prediction!**")
