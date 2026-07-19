"""Image preprocessing and model inference for PlantMD."""

import numpy as np
from tensorflow.keras.utils import img_to_array, load_img

IMAGE_SIZE = (224, 224)

LABELS: dict[str, int] = {
    "Apple Scab": 0,
    "Apple Black rot": 1,
    "Apple Cedar rust": 2,
    "Apple healthy": 3,
    "Blueberry healthy": 4,
    "Cherry(Sour) Mildew": 5,
    "Cherry(Sour) healthy": 6,
    "Corn Leaf spot": 7,
    "Corn Common rust": 8,
    "Corn Northern Leaf Blight": 9,
    "Corn healthy": 10,
    "Grape Black rot": 11,
    "Grape Black measles": 12,
    "Grape Leaf Blight": 13,
    "Grape healthy": 14,
    "Citrus greening": 15,
    "Peach Bacterial spot": 16,
    "Peach healthy": 17,
    "Bell_Pepper Bacterial spot": 18,
    "Bell_Pepper healthy": 19,
    "Potato Early Blight": 20,
    "Potato Late Blight": 21,
    "Potato healthy": 22,
    "Raspberry healthy": 23,
    "Soybean healthy": 24,
    "Squash Powdery mildew": 25,
    "Strawberry Leaf scorch": 26,
    "Strawberry healthy": 27,
    "Tomato Bacterial spot": 28,
    "Tomato Early blight": 29,
    "Tomato Late blight": 30,
    "Tomato Leaf Mold": 31,
    "Tomato Septoria leaf spot": 32,
    "Tomato Two-spotted spider mite": 33,
    "Tomato Target Spot": 34,
    "Tomato Yellow Leaf Curl Virus": 35,
    "Tomato mosaic virus": 36,
    "Tomato healthy": 37,
}

_INDEX_TO_LABEL = {index: label for label, index in LABELS.items()}


def preprocess_image(image_source) -> np.ndarray:
    """Load an image (path or file-like object) into a normalized model-ready batch."""
    img = load_img(image_source, target_size=IMAGE_SIZE)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return x / 255


def predict_top_k(preprocessed_image: np.ndarray, model, k: int = 3) -> list[tuple[str, float]]:
    """Run inference and return the top-k (label, confidence_pct) pairs, descending."""
    predictions = model.predict(preprocessed_image)[0]
    top_indices = np.argsort(predictions)[-k:]
    ranked = [(_INDEX_TO_LABEL[i], round(float(predictions[i]) * 100, 3)) for i in top_indices]
    return sorted(ranked, key=lambda pair: pair[1], reverse=True)
