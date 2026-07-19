"""Cached model loading for PlantMD."""

from pathlib import Path

import streamlit as st
import tensorflow as tf


@st.cache_resource(show_spinner="Loading model...")
def load_model(model_path: str | Path) -> tf.keras.Model:
    """Load the trained Keras model, cached across Streamlit reruns."""
    if not Path(model_path).exists():
        raise FileNotFoundError(
            f"Model weights not found at {model_path}. Run `git lfs pull` to fetch them."
        )
    return tf.keras.models.load_model(model_path)
