#!/bin/bash

# #### local path for JPEG
# ORIGINAL_IMAGE_FOLDER_PATH=../data/test/original/
# COMPRESSED_IMAGE_FOLDER_PATH=../data/test/compressed/JPEG/
# RECONSTRUCTED_IMAGE_FOLDER_PATH=../data/test/reconstructed/JPEG/

# #### local path for JPEG2000
# ORIGINAL_IMAGE_FOLDER_PATH=../data/test/original/
# COMPRESSED_IMAGE_FOLDER_PATH=../data/test/compressed/JPEG2000/
# RECONSTRUCTED_IMAGE_FOLDER_PATH=../data/test/reconstructed/JPEG2000/

#### local path for HEIC (High Efficiency Image Container)
ORIGINAL_IMAGE_FOLDER_PATH=../data/test/original/
COMPRESSED_IMAGE_FOLDER_PATH=../data/test/compressed/HEIC/
RECONSTRUCTED_IMAGE_FOLDER_PATH=../data/test/reconstructed/HEIC/

# #### local path for Balle's approach in 2018
# ORIGINAL_IMAGE_FOLDER_PATH=../data/test/original/
# COMPRESSED_IMAGE_FOLDER_PATH=../data/test/compressed/balle2018/
# RECONSTRUCTED_IMAGE_FOLDER_PATH=../data/test/reconstructed/balle2018/

# #### local path for my approach
# ORIGINAL_IMAGE_FOLDER_PATH=../data/test/original/
# COMPRESSED_IMAGE_FOLDER_PATH=../data/test/compressed/my_approach/
# RECONSTRUCTED_IMAGE_FOLDER_PATH=../data/test/reconstructed/my_approach/


#### Calculate bpp (bit per pixel), PSNR (Peak-Signal-to-Noise-Ratio) and
#### MS-SSIM(Multi-Scale Structural Similarity) for single image compression

python3 batch_psnr.py \
  --original_path ${ORIGINAL_IMAGE_FOLDER_PATH} \
  --compressed_path ${COMPRESSED_IMAGE_FOLDER_PATH} \
  --reconstructed_path ${RECONSTRUCTED_IMAGE_FOLDER_PATH}
