app.py
import streamlit as st
import numpy as np
import random

st.title("Signature Forgery Detector (Demo)")

uploaded_file = st.file_uploader("Upload a signature image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.success("File uploaded successfully!")

            # Randomly predict Genuine or Forged just as a demo
                result = random.choice(["Genuine", "Forged"])
                    st.markdown(f"### Prediction: `{result}`")