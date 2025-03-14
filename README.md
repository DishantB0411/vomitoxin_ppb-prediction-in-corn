# Vomitoxin Prediction in Corn

## Overview
This repository contains a machine learning pipeline designed to predict **vomitoxin levels in corn** based on **hyperspectral imaging data**. The model processes spectral data, applies **Principal Component Analysis (PCA)** for dimensionality reduction, normalizes the transformed features, and predicts vomitoxin concentrations in **parts per billion (ppb)**.

## Features
- **Streamlit Web Application**: Users can upload spectral data or manually input values to get predictions.
- **Automated Preprocessing**: PCA transformation and MinMax scaling are applied before prediction.
- **Downloadable Predictions**: Users can download their results in CSV format.

## Installation
To run this project locally, install the required dependencies:
```bash
pip install -r requirements.txt
```
Ensure that `model_pipeline.pkl` (containing the trained model, PCA, and scaler) is placed in the root directory.

## Usage
Run the Streamlit app with:
```bash
streamlit run app.py
```
- **Upload a CSV/Excel file** with **448 spectral bands**.
- **Or manually input** comma-separated spectral values.
- Get a **vomitoxin concentration prediction**.
- Download results in CSV format.

## Methodology
1. **Data Preprocessing**
   - PCA transformation reduces high-dimensional spectral data.
   - MinMax scaling ensures normalized input to the model.
2. **Model Selection**
   - The trained model is stored in `model_pipeline.pkl`.
   - The pipeline applies **PCA + MinMax Scaling + Machine Learning Model**.
3. **Trade-offs & Challenges**
   - **Dimensionality Reduction**: PCA captures key spectral variations but may lose some information.
   - **Feature Engineering**: Selecting 448 bands ensures model generalizability but needs careful preprocessing.
   - **Error Handling**: Ensuring input compatibility with PCA is crucial.

## Results
- The model outputs **predicted vomitoxin levels** in ppb.
- Users can validate and analyze predictions through the provided web interface.

## Contribution
It's a Machine Learning Assignment. The approach is fine but need to work upon many improvements can be done.
Dishant Bothra

