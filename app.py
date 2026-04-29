import streamlit as st
import pandas as pd
from model import predict, model_name, accuracy

st.set_page_config(page_title="Eco Analyzer", layout="centered")

st.title("🌍 AI Eco Innovation Analyzer (Advanced)")
st.write("AI-powered sustainability analysis with model comparison")

# Input sliders
energy = st.slider("Energy Usage", 0, 100, 50)
waste = st.slider("Waste Produced", 0, 50, 20)
water = st.slider("Water Usage", 0, 100, 30)

# Show model info
st.info(f"Best Model: {model_name}")
st.info(f"Accuracy (R² Score): {accuracy:.2f}")

if st.button("Analyze"):
    result = predict(energy, waste, water)

    st.subheader(f"🌡 Predicted Carbon Emission: {result:.2f}")

    # Graph
    df = pd.DataFrame({
        "Parameter": ["Energy", "Waste", "Water"],
        "Value": [energy, waste, water]
    })
    st.bar_chart(df.set_index("Parameter"))

    # Smart Recommendations
    st.subheader("💡 AI Recommendations")

    if energy > 70:
        st.write("⚡ Reduce energy usage or switch to renewable sources")

    if waste > 25:
        st.write("🗑 Improve waste management and recycling")

    if water > 60:
        st.write("💧 Optimize water usage and reduce wastage")

    if result > 85:
        st.error("⚠ High Pollution Risk")
    elif result > 60:
        st.warning("⚡ Moderate Pollution Level")
    else:
        st.success("✅ Sustainable System")
