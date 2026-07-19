import csv

import numpy as np
import pytest
from PIL import Image

from plantmd.inference import LABELS


@pytest.fixture
def synthetic_image_path(tmp_path):
    """A tiny synthetic RGB image, avoiding a dependency on the real example JPEGs."""
    path = tmp_path / "leaf.png"
    Image.new("RGB", (50, 50), color=(34, 139, 34)).save(path)
    return path


class FakeModel:
    """Stands in for the real Keras model: returns a deterministic (1, 38) prediction."""

    def predict(self, x):
        predictions = np.zeros((1, len(LABELS)))
        predictions[0, LABELS["Tomato healthy"]] = 0.7
        predictions[0, LABELS["Tomato Early blight"]] = 0.2
        predictions[0, LABELS["Tomato Late blight"]] = 0.1
        return predictions


@pytest.fixture
def fake_model():
    return FakeModel()


@pytest.fixture
def tmp_descriptions_csv(tmp_path):
    """A small descriptions CSV containing a description with an embedded comma."""
    path = tmp_path / "disease_description.csv"
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["label", "description"])
        writer.writerow(["Apple Scab", "Apple scab affects leaves and fruit."])
        writer.writerow(
            [
                "Corn Leaf spot",
                "Symptoms are sometimes confused with northern leaf blight, "
                "southern leaf blight, and anthracnose.",
            ]
        )
    return path
