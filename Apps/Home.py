import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Home | Real Estate Price Prediction", page_icon="🏠", layout="wide")

# --- Main Title ---
st.title("🏠 Real Estate Price Prediction App")

# --- Intro Section ---
st.markdown(
    """
    Welcome to the **Real Estate Price Prediction App**.  

    This application helps you:
    - ✅ Predict house prices based on property features  
    - 📊 Analyze market trends and insights  
    - 🧠 Explore model performance in an interactive way  

    Use the **sidebar** to navigate between:
    - **Prediction Page** → Enter property details and get instant predictions  
    - **Analytics Page** → Explore visual insights from the data  
    """
)

# --- Add Columns for Highlights ---
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 High accuracy model for price prediction")
with col2:
    st.info("📉 Optimized with advanced ML algorithms")
with col3:
    st.info("⚡ Fast, interactive, and user-friendly")

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    💡 *Tip: Start by visiting the **Prediction Page** from the sidebar 
    to estimate the price of a property.*
    """
)