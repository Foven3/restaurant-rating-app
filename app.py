import streamlit as st
from pages import home, prediction, about

st.set_page_config(page_title="Restaurant Rating Predictor", page_icon="🍴", layout="wide")

# Main navigation inside the app (not sidebar)
st.title("🍴 Restaurant Rating Predictor")

# Use buttons or tabs for navigation
nav = st.radio(
    "Navigation",
    ["Home", "Prediction", "About"],
    horizontal=True   # 👈 makes it appear across the top
)

if nav == "Home":
    home.show()
elif nav == "Prediction":
    prediction.show()
elif nav == "About":
    about.show()
