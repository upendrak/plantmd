# Build the model weights via `git lfs pull` before running `docker build .` —
# .gitattributes tracks models/model_vgg16_2.hdf5 through Git LFS, and a plain
# `git clone` only fetches the LFS pointer file, not the real weights.

FROM python:3.11-slim-bookworm AS builder

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PIP_NO_CACHE_DIR=1

WORKDIR /build

COPY pyproject.toml ./
COPY src/ ./src/
RUN pip install --prefix=/install .

FROM python:3.11-slim-bookworm

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash appuser

COPY --from=builder /install /usr/local

WORKDIR /app
COPY app.py ./
COPY models/ ./models/
COPY .streamlit/ ./.streamlit/

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
