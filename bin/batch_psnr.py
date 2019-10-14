import tensorflow as tf
import numpy
import math
import cv2
import os
import logging
from os import listdir
from os.path import isfile, join
from absl import flags

flags.DEFINE_string("original_path", default=None,
                  help="Path for folder containing original image files.")
flags.DEFINE_string("compressed_path", default=None,
                     help="Path for folder containing compressed image files.")
flags.DEFINE_string("reconstructed_path", default=None,
                     help="Path for folder containing reconstructed image files.")
FLAGS = flags.FLAGS

def get_batch_bpp_psnr_msssim():
    avg_psnr = 0
    avg_bpp = 0
    avg_msssim = 0
    try:
        original_files = [f for f in listdir(FLAGS.original_path) if isfile(join(FLAGS.original_path, f))]
        compare_files = [f for f in listdir(FLAGS.reconstructed_path) if isfile(join(FLAGS.reconstructed_path, f))]
        bin_files = [f for f in listdir(FLAGS.compressed_path) if isfile(join(FLAGS.compressed_path, f))]
        sess = tf.Session()
        for i in range(0, len(original_files)):
            original_img = original_files[i]
            compare_img = compare_files[i]
            bin_file = bin_files[i]
            original = cv2.imread(FLAGS.original_path + original_img)
            contrast = cv2.imread(FLAGS.reconstructed_path + compare_img)
            original = numpy.expand_dims(original, axis=0)
            contrast = numpy.expand_dims(contrast, axis=0)
            original_tensor = tf.convert_to_tensor(original, dtype=tf.uint8)
            contrast_tensor = tf.convert_to_tensor(contrast, dtype=tf.uint8)
            msssim_tensor = tf.image.ssim_multiscale(original_tensor,contrast_tensor,255)
            psnr_tensor = tf.image.psnr(original_tensor, contrast_tensor, 255)
            msssim = sess.run(msssim_tensor)
            psnr = sess.run(psnr_tensor)
            first,h,w,bpp = numpy.shape(contrast)
            bpp = os.path.getsize(FLAGS.compressed_path + bin_file) * 8 / (h * w)
            avg_bpp += bpp
            avg_psnr += psnr
            avg_msssim += msssim
        avg_bpp /= len(original_files)
        avg_psnr /= len(original_files)
        avg_msssim /= len(original_files)
    except Exception as e:
        logging.error(e)
    if avg_psnr == 0:
        print('Error occurs, please check log for details.')
    else:
        print ('average psnr: ', avg_psnr, '\n',
              'average ms_ssim: ', avg_msssim, '\n',
              'average bpp: ', avg_bpp)

def main(_):
    get_batch_bpp_psnr_msssim()

if __name__ == '__main__':
    tf.app.run()
