"""PlantMD Streamlit app: upload a leaf image, get a disease prediction."""

from pathlib import Path

import streamlit as st
from PIL import Image, UnidentifiedImageError

from plantmd.descriptions import format_description, load_descriptions
from plantmd.inference import predict_top_k, preprocess_image
from plantmd.model import load_model

MODEL_PATH = Path(__file__).parent / "models" / "model_vgg16_2.hdf5"
DESCRIPTIONS_PATH = Path(__file__).parent / "models" / "disease_description.csv"

st.set_page_config(page_title="PlantMD", page_icon="🌿", layout="centered")

st.markdown(
    "<h1 style='text-align: left; color: green;'>Welcome to PlantMD!</h1>", unsafe_allow_html=True
)
st.write("")

st.sidebar.title("Predict New Images")
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        image.verify()
        uploaded_file.seek(0)
        image = Image.open(uploaded_file)
    except UnidentifiedImageError:
        st.error("That file doesn't look like a valid image. Please upload a PNG or JPEG.")
        st.stop()

    st.image(image, caption="Uploaded image", use_container_width=True)

    try:
        model = load_model(MODEL_PATH)
    except FileNotFoundError as exc:
        st.error(str(exc))
        st.stop()

    uploaded_file.seek(0)
    processed_image = preprocess_image(uploaded_file)
    predictions = predict_top_k(processed_image, model)

    st.write("### Predictions")
    st.table(
        {
            "Class": [label for label, _ in predictions],
            "Confidence (%)": [confidence for _, confidence in predictions],
        }
    )

    descriptions = load_descriptions(DESCRIPTIONS_PATH)
    header, body = format_description(predictions[0], descriptions)
    st.write("### Description")
    st.info(f"**{header}**\n\n{body}")
else:
    st.markdown("""
        PlantMD is a web app that can rapidly and accurately diagnose plant diseases

        👈 Upload an image on the left to see how PlantMD can diagnose diseases for you!

        ### Want to learn more about PlantMD?

        - Checkout the [GitHub repo](https://github.com/upendrak/plantmd)
        """)
