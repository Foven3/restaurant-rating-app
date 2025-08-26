import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go

# ✅ Page setup
st.set_page_config(page_title="Restaurant Rating Predictor", page_icon="🍴", layout="wide")

# ✅ Load model + scaler
scalar = joblib.load("scalar.pkl")
model = joblib.load("mlmodel.pkl")

# 🎨 Page styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 20px;
        }
        .stButton>button {
            background-color: #ff6b6b;
            color: white;
            font-size: 18px;
            border-radius: 12px;
            height: 3em;
            width: 100%;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #ff4757;
            transform: scale(1.02);
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Title
st.markdown("<h1 style='text-align: center;'>🍴 Restaurant Rating Predictions App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Enter restaurant details below and predict customer rating 📊</p>", unsafe_allow_html=True)
st.divider()

# 📊 Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        averageCost = st.number_input("💰 Estimated average cost for two", min_value=50, max_value=99999, value=1000, step=200)
        priceRange = st.select_slider("💵 Price Range (1 Cheapest, 4 Most Expensive)", options=[1, 2, 3, 4], value=2)

    with col2:
        tableBooking = st.radio("📅 Table Booking?", ["Yes", "No"], horizontal=True)
        hasOnlineDelivery = st.radio("📦 Online Delivery?", ["Yes", "No"], horizontal=True)

    predictButton = st.form_submit_button("🔮 Predict Rating")

st.divider()

# 🔎 Prediction & Visualization
if predictButton:
    bookingStatus = 1 if tableBooking == "Yes" else 0
    deliveryStatus = 1 if hasOnlineDelivery == "Yes" else 0
    X = scalar.transform([[averageCost, bookingStatus, deliveryStatus, priceRange]])
    prediction = model.predict(X)[0]

    # 🎉 Prediction result
    st.markdown("### 📝 Prediction Result")
    if prediction < 2.5: 
        st.error("😞 Poor — Customers likely won’t be happy.")
        st.snow()
    elif prediction < 3.5:
        st.warning("😐 Average — Some improvements needed.")
        st.snow()
    elif prediction < 4:
        st.success("🙂 Good — Most customers will be satisfied.")
        st.balloons()
    elif prediction < 4.5:
        st.info("😃 Very Good — Great experience overall!")
        st.balloons()
    else:
        st.success("🤩 Excellent — Highly recommended!")
        st.balloons()

    # 📊 Plotly interactive bar chart
    fig = go.Figure(go.Bar(
        x=['Predicted Rating'],
        y=[prediction],
        marker_color='#ff6b6b',
        text=[f"{prediction:.2f}"],
        textposition='auto'
    ))
    fig.update_layout(
        yaxis=dict(range=[0,5]),
        title="Predicted Customer Rating",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig)
