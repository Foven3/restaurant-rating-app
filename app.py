import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Restaurant Rating Predictor", page_icon="🍴", layout="wide")

# Load scaler and model
scalar = joblib.load("scalar.pkl")
model = joblib.load("mlmodel.pkl")

# 🎯 Title (centered)
st.markdown("<h1 style='text-align: center;'>🍴 Restaurant Rating Predictions App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Predict how good a restaurant review might be!</h3>", unsafe_allow_html=True)
st.divider()

# 📊 Inputs
averageCost = st.number_input("💰 Estimated average cost for two", min_value=50, max_value=99999, value=1000, step=200)
tableBooking = st.selectbox("📅 Restaurant has table booking?", ["Yes","No"])
hasOnlineDelivery = st.selectbox("📦 Restaurant has online booking?", ["Yes","No"])
priceRange = st.selectbox("💵 What is the price range? (1 Cheapest, 4 Most Expensive)", [1,2,3,4])

predictButton = st.button("🔮 Predict the review!")
st.divider()

# 🔎 Prepare data
bookingStatus = 1 if tableBooking == "Yes" else 0
deliveryStatus = 1 if hasOnlineDelivery == "Yes" else 0
X = scalar.transform([[averageCost, bookingStatus, deliveryStatus, priceRange]])

# 🎉 Prediction
if predictButton:
    prediction = model.predict(X)[0]

    if prediction < 2.5: 
        st.markdown("<h2 style='text-align: center; color: red;'>😞 Poor</h2>", unsafe_allow_html=True)
        st.snow()
    elif prediction < 3.5:
        st.markdown("<h2 style='text-align: center; color: orange;'>😐 Average</h2>", unsafe_allow_html=True)
        st.snow()
    elif prediction < 4:
        st.markdown("<h2 style='text-align: center; color: green;'>🙂 Good</h2>", unsafe_allow_html=True)
        st.balloons()
    elif prediction < 4.5:
        st.markdown("<h2 style='text-align: center; color: blue;'>😃 Very Good</h2>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown("<h2 style='text-align: center; color: purple;'>🤩 Excellent</h2>", unsafe_allow_html=True)
        st.balloons()
  