# The training dataset described in paper "VARIATIONAL IMAGE COMPRESSION
# WITH A SCALE HYPERPRIOR" comprised approximately 1 million images scraped
# from the world wide web. But the paper didn't release the exact dataset.

# My previous research proved that the autoencoder model can converge on a very
# small dataset containing only 139 images, and still generalize well on test
# dataset with very different image content.

# To optimize model performance in compressing photos of natural scenes, which
# is the also the optimization goal of traditional approaches like JPEG, I
# selected a training dataset focusing on photos in the wild.

# The training and validation dataset is CLIC(Challenge on Learned Image
# Compression) Dataset P("professional"), which is 1.9GB, and contains 2000
# well-representative photos in the wild with resolution higher than 2K.

# The script will download CLIC dataset into enas-image-compression/data/raw

# Run this bash script at path enas-image-compression/bin/ with the command:
# ''' bash ./scripts/data_ingestion.sh '''


# wget https://data.vision.ee.ethz.ch/cvl/clic/professional_train.zip -O ../data/raw/professional_train.zip
# unzip ../data/raw/professional_train.zip -d ../data/raw/professional_train
# wget https://data.vision.ee.ethz.ch/cvl/clic/professional_valid.zip -O ../data/raw/professional_valid.zip
# unzip ../data/raw/professional_valid.zip -d ../data/raw/professional_valid
wget https://data.vision.ee.ethz.ch/cvl/clic/mobile_train.zip -O ../data/raw/mobile_train.zip
unzip ../data/raw/mobile_train.zip -d ../data/raw/mobile_train
wget https://data.vision.ee.ethz.ch/cvl/clic/mobile_valid.zip -O ../data/raw/mobile_valid.zip
unzip ../data/raw/mobile_valid.zip -d ../data/raw/mobile_valid
