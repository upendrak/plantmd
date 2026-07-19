<!--
Template for deploying PlantMD as a Hugging Face Space.

Hugging Face Spaces reads deployment metadata from YAML frontmatter at the
top of THAT Space's own README.md (a separate git repo from this one, created
when you make the Space — optionally synced from this GitHub repo). Putting
this frontmatter into the main repo's README.md would just render as a raw
block on GitHub, so it lives here instead as a copy-in template.

To use: create a new Space at huggingface.co/new-space with SDK "Streamlit",
then replace its generated README.md with the content below (update the
`your-username` placeholder), and push this repo's contents to it.
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

See [github.com/your-username/plantmd](https://github.com/your-username/plantmd)
for the full source and Docker/local setup instructions.

Note: the trained model weights (`models/model_vgg16_2.hdf5`) are tracked
with Git LFS. If this Space is synced from a GitHub mirror, make sure LFS
objects are included in the sync, or upload the weights file directly through
the Hugging Face Space's file interface.
