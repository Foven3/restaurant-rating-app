import streamlit as st
import joblib
import plotly.graph_objects as go

# Load model & scaler
scalar = joblib.load("scalar.pkl")
model = joblib.load("mlmodel.pkl")

def show():
    st.title("🔮 Prediction Page")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            averageCost = st.number_input("💰 Estimated average cost for two", min_value=50, max_value=99999, value=1000, step=200)
            priceRange = st.select_slider("💵 Price Range (1 Cheapest, 4 Most Expensive)", options=[1, 2, 3, 4], value=2)

        with col2:
            tableBooking = st.radio("📅 Table Booking?", ["Yes", "No"], horizontal=True)
            hasOnlineDelivery = st.radio("📦 Online Delivery?", ["Yes", "No"], horizontal=True)

        predictButton = st.form_submit_button("🔮 Predict Rating")

    if predictButton:
        bookingStatus = 1 if tableBooking == "Yes" else 0
        deliveryStatus = 1 if hasOnlineDelivery == "Yes" else 0
        X = scalar.transform([[averageCost, bookingStatus, deliveryStatus, priceRange]])
        prediction = model.predict(X)[0]

        st.markdown("### 📝 Prediction Result")
        st.success(f"Predicted Rating: {prediction:.2f}")

        # --- Rating categories ---
        if prediction <= 2.5:
            rating_labelP = "❌ Poor"
            st.error(rating_labelP)
            st.snow()
        elif prediction <= 3.5:
            rating_labelA = "😕 Average"
            st.warning(rating_labelA)
            st.snow()
        elif prediction <= 4.0:
            rating_labelG = "🙂 Good"
            st.info(rating_labelG)
            st.balloons()
        elif prediction <= 4.5:
            rating_labelVG = "😃 Very Good"
            st.success(rating_labelVG)
            st.balloons()
        else:
            rating_labelE = "🌟 Excellent"
            st.success(rating_labelE)
            st.balloons()

        # Plotly chart
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
