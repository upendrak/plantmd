"""PlantMD: plant disease classification from leaf images."""

import os

# tensorflow>=2.16 defaults tf.keras to Keras 3, which can't load the HDF5
# models saved under the old Keras 2 API (like models/model_vgg16_2.hdf5).
# The tf_keras package restores the legacy Keras 2 implementation. This must
# be set before tensorflow is imported anywhere in the process, which is
# guaranteed here since Python always runs a package's __init__.py before
# any of its submodules.
os.environ.setdefault("TF_USE_LEGACY_KERAS", "1")
