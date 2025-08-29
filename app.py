import streamlit as st
from pages import home, prediction, about

st.set_page_config(page_title="Restaurant Rating Predictor", page_icon="🍴", layout="wide")

# Sidebar for navigation
st.title("Navigation")
page = st.radio("Go to", ["Home", "Prediction", "About"])

if page == "Home":
    home.show()
elif page == "Prediction":
    prediction.show()
elif page == "About":
    about.show()
