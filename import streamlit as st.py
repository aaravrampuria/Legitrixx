import streamlit as st
import numpy as np
import random

st.set_page_config(page_title="Signature Forgery Detector", layout="centered")

st.title("Signature Forgery Detector (Demo)")

uploaded = st.file_uploader("Upload a signature image", type=["png", "jpg", "jpeg"])
if not uploaded:
    st.info("Please upload an image.")
    else:
        st.image(uploaded, caption="Uploaded Image", use_column_width=True)
            # Demo prediction—replace with real model later
                result = random.choice(["Genuine", "Forged"])
                    st.markdown(f"## Prediction: **{result}**")