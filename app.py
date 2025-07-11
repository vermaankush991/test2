import numpy as np
import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('house_price_model.pkl', 'rb'))

# Title
st.title("🏠 Melbourne House Price Predictor")

# User inputs
car = float(st.text_input("Number of Car Parking Spaces:", "2"))
landsize = float(st.text_input("Land Size (m²):", "400"))
building_area = float(st.text_input("Building Area (m²):", "160"))
year_built = float(st.text_input("Year Built:", "1995"))

# Prepare input
input_data = np.array([[car, landsize, building_area, year_built]])

# Predict
predicted_price = model.predict(input_data)[0]

# Output
st.write(f"### 💰 Predicted House Price: **${predicted_price:,.2f} AUD**")
