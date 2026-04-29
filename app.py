import streamlit as st
from model import predict

# Page settings
st.set_page_config(page_title="Eco Analyzer", layout="centered")

st.title("🌍 AI Eco Innovation Analyzer")
st.write("Analyze environmental impact and get suggestions")

# Inputs
energy = st.slider("Energy Usage", 0, 100, 50)
waste = st.slider("Waste Produced", 0, 50, 20)
water = st.slider("Water Usage", 0, 100, 30)

# Button
if st.button("Analyze"):
    result = predict(energy, waste, water)

    st.subheader(f"🌡 Predicted Carbon Emission: {result:.2f}")

    # Suggestions
    if result > 85:
        st.error("⚠ High Pollution Level")
        st.write("• Switch to renewable energy")
        st.write("• Reduce industrial waste")
        st.write("• Optimize water usage")

    elif result > 60:
        st.warning("⚡ Moderate Pollution")
        st.write("• Improve efficiency")
        st.write("• Use eco-friendly processes")

    else:
        st.success("✅ Low Pollution - Sustainable System")
