import streamlit as st

def show():
    st.header("ℹ️ About")
    
    st.subheader("What is this app?")
    st.write(
        """
        The **Restaurant Rating Predictor** is a web application that estimates customer ratings for restaurants across the globe.  
        Based on features like Estimated average cost for two,  Price Range, Has table booking,and has online delivery, our model helps restaurant owners, food lovers, 
        and data enthusiasts understand what factors drive ratings.
        """
    )

    st.subheader("🌍 Data Source")
    st.write(
    """
    We utilize a publicly available dataset from Kaggle, named **Sales Prediction Dataset** [source](https://www.kaggle.com/datasets/mohdshahnawazaadil/sales-prediction-dataset), authored by Mohd Shahnawaz Aadil.  
    """
    )
    

    st.subheader("🧠 Technology Used")
    st.write(
        """
        - **Streamlit** for building the interactive web interface.  
        - **scikit-learn**, **NumPy**, **pandas** for data processing and modeling.  
        - **Machine Learning Models** like Linear Regression, Random Forest, or more advanced algorithms to estimate ratings.  
        """
    )

    st.subheader("⚠️ Limitations")
    st.write(
        """
        - Predictions are approximate and rely on the quality of the data used.  
        - Current data may not reflect real-world restaurant behaviors or ratings directly.
        """
    )

    st.subheader("🚀 Future Enhancements")
    st.write(
        """
        - Integrate restaurant-specific datasets (e.g., from Yelp, Zomato, etc.) to improve relevance and accuracy.  
        - Include richer features like user reviews, ratings trends, and operational metrics.  
        - Expand model capabilities using advanced techniques like deep learning.
        """
    )

    st.subheader("👩‍💻 Credits / Contact")
    st.write(
        """
        **Developed by:** Phyo Thiha (Foven)  
        Feel free to reach out at **foven0047@gmail.com** for feedback or collaboration!  

        **GitHub Repository:** [restaurant-rating-app](https://github.com/Foven3/restaurant-rating-app)
        """
    )

