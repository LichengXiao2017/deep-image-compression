# Run this script at directory enas-image-compression/bin, with command:
# ''' bash scripts/model_building.sh '''

# Train Balle2018 model on professional_train dataset from CLIC
TRAIN_DATA_PATH=../data/raw/professional_train/train
MODEL_PATH=../model
NUM_FILTERS=192
LAMBD=0.01
PREPROCESS_THREADS=16
TRAIN_BATCH_SIZE=8
MAX_TRAIN_STEPS=1E6

python balle2018.py \
--verbose \
--num_filters ${NUM_FILTERS} \
--checkpoint_dir ${MODEL_PATH} \
train \
--train_glob ${TRAIN_DATA_PATH}/*.png \
--lambda ${LAMBDA} \
--preprocess_threads ${PREPROCESS_THREADS} \
--batchsize ${TRAIN_BATCH_SIZE} \
--last_step ${MAX_TRAIN_STEPS}
