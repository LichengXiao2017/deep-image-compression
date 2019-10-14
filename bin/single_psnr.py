import tensorflow as tf
import numpy
import math
import cv2
import os
import logging
from os import listdir
from os.path import isfile, join
from absl import flags

flags.DEFINE_string("original_img", default=None,
                  help="Path for original image file.")
flags.DEFINE_string("compressed_img", default=None,
                     help="Path for compressed image file.")
flags.DEFINE_string("reconstructed_img", default=None,
                     help="Path for reconstructed image file.")
FLAGS = flags.FLAGS

def get_psnr_msssim_bpp():
    psnr = 0
    msssim = 0
    bpp = 0
    try:
        sess = tf.Session()
        original = cv2.imread(FLAGS.original_img)
        contrast = cv2.imread(FLAGS.reconstructed_img)
        original = numpy.expand_dims(original, axis=0)
        contrast = numpy.expand_dims(contrast, axis=0)
        original_tensor = tf.convert_to_tensor(original, dtype=tf.uint8)
        contrast_tensor = tf.convert_to_tensor(contrast, dtype=tf.uint8)
        msssim_tensor = tf.image.ssim_multiscale(
            original_tensor, contrast_tensor, 255)
        psnr_tensor = tf.image.psnr(original_tensor, contrast_tensor, 255)
        msssim = sess.run(msssim_tensor)
        psnr = sess.run(psnr_tensor)
        first, h, w, bpp = numpy.shape(contrast)
        bpp = os.path.getsize(FLAGS.compressed_img) * 8 / (h * w)
    except Exception as e:
        logging.error(e)
    if psnr == 0:
        print('Error occurs, please check log for details.')
    else:
        print('psnr: ', psnr, '\n',
              'ms_ssim: ', msssim, '\n',
              'bpp: ', bpp)

def main(_):
    get_psnr_msssim_bpp()

if __name__ == "__main__":
    tf.app.run()
