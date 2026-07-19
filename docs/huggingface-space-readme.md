<!--
Template for deploying PlantMD as a Hugging Face Space.

Hugging Face Spaces reads deployment metadata from YAML frontmatter at the
top of THAT Space's own README.md (a separate git repo from this one, created
when you make the Space — optionally synced from this GitHub repo). Putting
this frontmatter into the main repo's README.md would just render as a raw
block on GitHub, so it lives here instead as a copy-in template.

To use: create a new Space at huggingface.co/new-space with SDK "Streamlit",
then replace its generated README.md with the content below, and push this
repo's contents to it.
-->
---
title: PlantMD
emoji: 🌿
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
license: gpl-3.0
---

# PlantMD

PlantMD is an image-based plant disease classifier. Upload a photo of a leaf
and it predicts the most likely disease (or healthy) class out of 38
categories, along with a confidence score and description.

See [github.com/upendrak/plantmd](https://github.com/upendrak/plantmd) for
the full source and Docker/local setup instructions.

The trained model weights are hosted separately on the
[upendrad/plantmd](https://huggingface.co/upendrad/plantmd) model repo on
Hugging Face Hub, and downloaded automatically the first time the app runs —
nothing to sync or upload manually here.
