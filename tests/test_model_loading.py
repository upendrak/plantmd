from pathlib import Path

import pytest

from plantmd.model import load_model

REAL_MODEL_PATH = Path(__file__).parent.parent / "models" / "model_vgg16_2.hdf5"


def test_load_model_raises_helpful_error_for_missing_file(tmp_path):
    missing_path = tmp_path / "does_not_exist.hdf5"
    with pytest.raises(FileNotFoundError, match="git lfs pull"):
        load_model(missing_path)


@pytest.mark.skipif(
    not REAL_MODEL_PATH.exists() or REAL_MODEL_PATH.stat().st_size < 1_000_000,
    reason="real model weights not pulled via git-lfs in this environment",
)
def test_load_model_loads_real_weights():
    model = load_model(REAL_MODEL_PATH)
    assert model is not None
