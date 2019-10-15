# -*- coding: utf-8 -*-
# Copyright 2019 Licheng Xiao. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

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


class SingleEvaluator:
    def get_psnr_msssim_bpp(self, original_img, reconstructed_img, compressed_img):
        psnr = 0
        msssim = 0
        bpp = 0
        try:
            sess = tf.Session()
            original = cv2.imread(original_img)
            contrast = cv2.imread(reconstructed_img)
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
            bpp = os.path.getsize(compressed_img) * 8 / (h * w)
        except Exception as e:
            logging.error(e)
        if psnr == 0:
            logging.error('Error occurs, please check log for details.')
        else:
            logging.info('psnr: ', psnr, '\n',
                         'ms_ssim: ', msssim, '\n',
                         'bpp: ', bpp)
            return psnr, msssim, bpp


def main(_):
    single_evaluator = SingleEvaluator()
    single_evaluator.get_psnr_msssim_bpp(FLAGS.original_img,
                                         FLAGS.reconstructed_img,
                                         FLAGS.compressed_img)


if __name__ == "__main__":
    tf.app.run()
