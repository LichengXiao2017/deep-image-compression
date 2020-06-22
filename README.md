## [Project Demo Slides](https://bit.ly/deepimagecompressionslides)
## [Package](https://pypi.org/project/deep-image-compression/)

# Deep Image Compression: Extreme Image Compression Using Deep Learning
![image of pipline](https://github.com/LichengXiao2017/deep-image-compression/blob/master/deep_image_compression/static/img/pipeline.png)

Deep Image Compression is an end-to-end tool for extreme image compression
using deep learning. It outperforms JEPG, HEIC(state-of-the-art traditional
image compression method, derived from H.265, available in iPhone and Mac) and
Balle's approach in 2018 (state-of-the-art open source deep learning approach,
proposed by Balle et al in "Variational Image Compression with a Scale
Hyperprior").

The baseline model and algorithm(Balle2018) was cloned from the [Data
compression in TensorFlow](https://github.com/tensorflow/compression) repo in
September, 2019.

In my approach, I changed the training dataset, and modified the model
structure, as is shown in the following figure.

![image of model structure modification](https://github.com/LichengXiao2017/deep-image-compression/blob/master/deep_image_compression/static/img/model_improvement.png)

## The directory structure of this repo is the following:
- **deep-image-compression** : contains all the source code
  - **bin** : contains all executable scripts
  - **model** : contains model checkpoints
  - **static** : contains images used in the README.md
- **tests** : contains all the unit tests
- **data** : contains data for training, validation and unit test
- **configs** : contains config files for hyperparameters during training and evaluation
- **docs** : contains documentations
- **examples** : contains jupyter notebook examples of the workflow



## Setup

#### Installation
First, clone this github repo.
```
git clone https://github.com/LichengXiao2017/deep-image-compression.git
cd deep-image-compression
```
Then, install deep-image-compression package. You can install it within venv or
with --user option.
```
python3 -m pip install deep-image-compression --user
```
#### Requisites
All the following requisites will be automatically installed when you install
the deep-image-compression package.
1. 'tensorflow-gpu==1.15.0-rc1',
2. 'absl-py==0.8.0',
3. 'opencv-python==4.1.1.26',
4. 'argparse==1.4.0',
5. 'glob3==0.0.1',
6. 'tensorflow_compression==1.2',
7. 'numpy==1.16.4',

#### Environment setup
It's highly recommended that workstation running this repo to have at least 1
GPU. The repo has been tested on Nvidia GTX 1070 (8GB memory).
The repo currently support only single GPU. It's suggested that you specify
the GPU you are going to use before running the scripts. For example, if you
want to use the first GPU, type the following command in terminal.
```
export CUDA_VISIBLE_DEVICES=0
```
Other processes running on this GPU might cause problem, so please run this
repo on a vacant GPU.

## Steps to run

### Step1: Configuration
Configurations are not combined into single config file yet.
Here are a list of scripts and variables that need configuration before running:
1. bin/data_ingestion
      - DATA_PATH
2. bin/data_processing
      - IMAGE_PATH
3. bin/model_training_balle2018
      - TRAIN_DATA_PATH
      - MODEL_PATH
      - LAMBDA
      - NUM_FILTERS
      - MAX_TRAIN_STEPS
4. bin/model_training_my_approach
      - TRAIN_DATA_PATH
      - MODEL_PATH
      - LAMBDA
      - NUM_FILTERS
      - MAX_TRAIN_STEPS
      - MAIN_LEARNING_RATE
      - AUX_LEARNING_RATE
      - TRAIN_BATCH_SIZE
5. bin/model_inference_compress_balle2018
      - TEST_DATA_PATH
      - MODEL_PATH
      - NUM_FILTERS
6. bin/model_inference_compress_my_approach
      - TEST_DATA_PATH
      - MODEL_PATH
      - NUM_FILTERS
7. bin/model_inference_decompress_my_approach
      - TEST_DATA_PATH
      - MODEL_PATH
      - NUM_FILTERS
8. bin/model_inference_decompress_my_approach
      - TEST_DATA_PATH
      - MODEL_PATH
      - NUM_FILTERS
9. bin/rename_reconstructed_images
      - RECONSTRUCTED_IMAGE_PATH
10. bin/model_analysis_single_image
      - ORIGINAL_IMAGE_PATH
      - COMPRESSED_IMAGE_PATH
      - RECONSTRUCTED_IMAGE_PATH
11. bin/model_analysis_batch_images
      - ORIGINAL_IMAGE_FOLDER_PATH
      - COMPRESSED_IMAGE_FOLDER_PATH
      - RECONSTRUCTED_IMAGE_FOLDER_PATH

In the future, these configurations will be combined into single config file
under configs/

### Step2: Prepare and Preprocess
#### - Download dataset
Download and unzip the dataset you want to use for training by running:
```
bin/data_ingestion
```

The datasets used in this project is:
- **The [CLIC dataset](https://www.compression.cc)**
You can also modify data_ingestion and use your own training dataset.

#### - Convert color domain to RGB
This repo currently support only RGB color domain.
Convert the dataset to RGB domain by running:
```
bin/data_processing
```
### Step3: Train model
To train the baseline (Balle2018) model, run:
```
bin/model_training_balle2018
```
To train my approach model, run:
```
bin/model_training_my_approach
```
### Step4: Inference model
Compression will convert a .png file to .png.tfci file.
To compress image using Balle2018 model, run:
```
bin/model_inference_compress_balle2018
```
To compress image using my approach model, run:
```
bin/model_inference_compress_my_approach
```

Decompression will convert a .png.tfci file to .png.tfci.png file.
To decompress image using Balle2018 model, run:
```
bin/model_inference_decompress_balle2018
```
To decompress image using my approach model, run:
```
bin/model_inference_decompress_my_approach
```

### Step5: Evaluate model
#### rename decompressed images
To maintain the same order of files when evaluating a list of images, you need
to rename .png.tfci.png files into .png files before evaluation, run:
```
bin/rename_reconstructed_images
```
#### evaluate single image
```
bin/model_analysis_single_image
```
#### evaluate a list images
```
bin/model_analysis_batch_images
```


## Analysis

#### Final result:

The following graphs show that my approach achieved lower bpp(bit per pixel) with
similar MSE(mean square error) during training.
![image of MSE comparison](https://github.com/LichengXiao2017/deep-image-compression/blob/master/deep_image_compression/static/img/MSE_comparison.png)

![image of bpp comparison](https://github.com/LichengXiao2017/deep-image-compression/blob/master/deep_image_compression/static/img/bpp_comparison.png)

Note:
1. The metrics in the table is averaged on all images from Kodak dataset
2. The encoding and decoding time are manually recorded

![image of results](https://github.com/LichengXiao2017/deep-image-compression/blob/master/deep_image_compression/static/img/result_table.png)
