"""Cached model loading for PlantMD.

The trained weights are not committed to this repo. They're hosted on
Hugging Face Hub and downloaded on first use, then cached locally.
"""

from pathlib import Path

import streamlit as st
import tensorflow as tf
from huggingface_hub import hf_hub_download

HF_REPO_ID = "upendrak/plantmd"


@st.cache_resource(show_spinner="Loading model...")
def load_model(local_path: str | Path) -> tf.keras.Model:
    """Load the trained Keras model, fetching it from Hugging Face Hub if not present locally."""
    local_path = Path(local_path)
    if not local_path.exists():
        local_path = _fetch_weights(local_path)
    return tf.keras.models.load_model(local_path)


def _fetch_weights(local_path: Path) -> Path:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        downloaded = hf_hub_download(
            repo_id=HF_REPO_ID,
            filename=local_path.name,
            local_dir=local_path.parent,
        )
    except Exception as exc:
        # Any download failure (missing repo, no network, rate limit, ...) should
        # surface as one clear message rather than a raw huggingface_hub traceback.
        raise FileNotFoundError(
            f"Could not download model weights from Hugging Face Hub "
            f"({HF_REPO_ID}/{local_path.name}): {exc}"
        ) from exc
    return Path(downloaded)
