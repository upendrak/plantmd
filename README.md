# PlantMD

[![CI](https://github.com/upendrak/plantmd/actions/workflows/ci.yml/badge.svg)](https://github.com/upendrak/plantmd/actions/workflows/ci.yml)
[![PyPI - Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)]()
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

PlantMD is an image-based plant disease diagnosis web app. Upload a photo of a
leaf and it predicts the most likely disease (or healthy) class out of 38
categories, along with a confidence score and a short description.

The model is a VGG16 transfer-learning network trained on the 54,000-image
[PlantVillage](https://github.com/spMohanty/PlantVillage-Dataset) dataset,
augmented (mainly via rotation) to ~87,000 images to balance the originally
skewed class distribution, then split 80/20 into training and validation sets.

:point_down: Screenshots:

<p align="center">
  <img src="https://i.postimg.cc/K8yJxgj7/plantmd-ss-1.png" width="600px" alt="">
</p>

<p align="center">
  <img src="https://i.postimg.cc/P5RJ11DY/plantmd-ss-2.png" width="600px" alt="">
</p>

------------------

## Project layout

```
app.py                          # Streamlit entrypoint
src/plantmd/
  inference.py                  # preprocessing + top-k prediction
  descriptions.py                # disease description lookup
  model.py                        # cached model loading (downloads from HF Hub)
models/
  disease_description.csv        # per-class description text
tests/                           # pytest suite (no real model weights required)
```

Dependencies are declared in `pyproject.toml` (the source of truth). A root
`requirements.txt` is also kept, containing only `-e .`, purely because
Streamlit Community Cloud and Hugging Face Spaces auto-detect dependencies
from a root `requirements.txt` file rather than `pyproject.toml` — it installs
this project itself, so there's nothing to keep in sync by hand.

The trained model weights (`model_vgg16_2.hdf5`) are **not** committed to
this repo. They're hosted on [Hugging Face Hub](https://huggingface.co/upendrad/plantmd)
and downloaded automatically by `src/plantmd/model.py` the first time the app
runs, then cached under `models/` for subsequent runs. No Git LFS involved.

## Getting started locally

```shell
git clone https://github.com/upendrak/plantmd.git && cd plantmd
pip install -e .[dev]
streamlit run app.py
```

The first run downloads the model weights from Hugging Face Hub (a one-time
cost); after that they're read from the local `models/` cache. Open
http://localhost:8501/ and upload an image (a few samples are in
`example_images/`).

Run the test suite (works without the real model weights, using fakes/fixtures):

```shell
pytest
```

## Docker

```shell
docker build -t plantmd .
docker run --rm -p 8501:8501 plantmd
```

Open http://localhost:8501/. The container downloads the model weights from
Hugging Face Hub on its first run (needs outbound internet access).

## Streamlit Community Cloud / Hugging Face Spaces

Both platforms can deploy directly from this repo:

- **Streamlit Community Cloud**: point a new app at this repo, branch
  `master`, main file `app.py`. It installs from `requirements.txt`
  automatically, and the model weights download from Hugging Face Hub on
  first run.
- **Hugging Face Spaces**: create a Space with SDK "Streamlit", then use
  [`docs/huggingface-space-readme.md`](docs/huggingface-space-readme.md) as a
  starting template for that Space's own `README.md` (Spaces require SDK
  metadata in the Space's README frontmatter, which is a separate file from
  this repo's README).

## License

GPLv3 — see [LICENSE](LICENSE).
