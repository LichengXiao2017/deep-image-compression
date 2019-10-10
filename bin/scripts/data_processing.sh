# The training dataset described in paper "VARIATIONAL IMAGE COMPRESSION
# WITH A SCALE HYPERPRIOR" comprised approximately 1 million images scraped
# from the world wide web.
# The preprocessing of original approach contains two steps:
  # 1. Images with excessive saturation were screened out to reduce the number of
  # non-photographic images.
  # 2. To reduce existing compression artifacts, the
  # images were further downsampled by a randomized factor, such that the
  # minimum of their height and width equaled between 640 and 1200 pixels.

# In my approach, I use 2000 high quality photos in the wild from CLIC, which
# eliminate the need for preprocessing as described in the original paper.

# When generating actual training dataset, the images are randomly sliced to
# small patches with default size of 256 x 256. This part of code is included in
# enas-image-compression/bin/deep_image_compression.sh
