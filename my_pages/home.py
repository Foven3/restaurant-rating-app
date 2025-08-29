import streamlit as st

def show():
    st.header("🏠 Home")
    st.subheader("Welcome to the Restaurant Rating Predictor 🍴")

    st.write(
        """
        This application uses restaurant data collected from **all over the world** 🌍 
        to predict customer ratings.  
        
        With a combination of factors such as Estimated average cost for two,  Price Range, Has table booking,and has online delivery, 
        our model provides insights into how restaurants are likely to be rated by their visitors.  

        Whether you are a restaurant owner, a food enthusiast, or just curious, 
        this tool allows you to explore patterns and predict ratings with ease.  
        """
    )

    st.success("👉 Use the navigation above to try predictions or learn more about the app.")
