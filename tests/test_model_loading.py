from pathlib import Path
from unittest.mock import Mock

import pytest
import tensorflow as tf

from plantmd import model as model_module
from plantmd.model import load_model

REAL_MODEL_PATH = Path(__file__).parent.parent / "models" / "model_vgg16_2.hdf5"


def test_load_model_uses_existing_local_file_without_downloading(tmp_path, monkeypatch):
    local_path = tmp_path / "weights.hdf5"
    local_path.write_bytes(b"placeholder file, just needs to exist")

    monkeypatch.setattr(
        model_module,
        "hf_hub_download",
        Mock(side_effect=AssertionError("should not attempt a download")),
    )
    monkeypatch.setattr(tf.keras.models, "load_model", Mock(return_value="fake-model"))

    assert load_model(local_path) == "fake-model"


def test_load_model_raises_helpful_error_when_download_fails(tmp_path, monkeypatch):
    missing_path = tmp_path / "does_not_exist.hdf5"
    monkeypatch.setattr(
        model_module, "hf_hub_download", Mock(side_effect=RuntimeError("network unreachable"))
    )

    with pytest.raises(FileNotFoundError, match="Hugging Face Hub"):
        load_model(missing_path)


@pytest.mark.skipif(
    not REAL_MODEL_PATH.exists() or REAL_MODEL_PATH.stat().st_size < 1_000_000,
    reason="real model weights not present locally",
)
def test_load_model_loads_real_weights():
    model = load_model(REAL_MODEL_PATH)
    assert model is not None
