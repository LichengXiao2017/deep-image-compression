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

flags.DEFINE_string("original_path", default=None,
                    help="Path for folder containing original image files.")
flags.DEFINE_string("compressed_path", default=None,
                    help="Path for folder containing compressed image files.")
flags.DEFINE_string("reconstructed_path", default=None,
                    help="Path for folder containing reconstructed image files.")
FLAGS = flags.FLAGS


class BatchEvaluator:
    def get_batch_bpp_psnr_msssim(self,
                                  original_path,
                                  reconstructed_path,
                                  compressed_path):
        avg_psnr = 0
        avg_bpp = 0
        avg_msssim = 0
        try:
            original_files = [f for f in listdir(
                original_path) if isfile(join(original_path, f))]
            compare_files = [f for f in listdir(reconstructed_path) if isfile(
                join(reconstructed_path, f))]
            bin_files = [f for f in listdir(compressed_path) if isfile(
                join(compressed_path, f))]
            sess = tf.Session()
            for i in range(0, len(original_files)):
                original_img = original_files[i]
                compare_img = compare_files[i]
                bin_file = bin_files[i]
                original = cv2.imread(original_path + original_img)
                contrast = cv2.imread(reconstructed_path + compare_img)
                original = numpy.expand_dims(original, axis=0)
                contrast = numpy.expand_dims(contrast, axis=0)
                original_tensor = tf.convert_to_tensor(
                    original, dtype=tf.uint8)
                contrast_tensor = tf.convert_to_tensor(
                    contrast, dtype=tf.uint8)
                msssim_tensor = tf.image.ssim_multiscale(
                    original_tensor, contrast_tensor, 255)
                psnr_tensor = tf.image.psnr(
                    original_tensor, contrast_tensor, 255)
                msssim = sess.run(msssim_tensor)
                psnr = sess.run(psnr_tensor)
                first, h, w, bpp = numpy.shape(contrast)
                bpp = os.path.getsize(
                    compressed_path + bin_file) * 8 / (h * w)
                avg_bpp += bpp
                avg_psnr += psnr
                avg_msssim += msssim
            avg_bpp /= len(original_files)
            avg_psnr /= len(original_files)
            avg_msssim /= len(original_files)
        except Exception as e:
            logging.error(e)
        if avg_psnr == 0:
            logging.error('Error occurs, please check log for details.')
        else:
            logging.info('average psnr: ', avg_psnr, '\n',
                         'average ms_ssim: ', avg_msssim, '\n',
                         'average bpp: ', avg_bpp)
            return avg_psnr, avg_msssim, avg_bpp


def main(_):
    batch_evaluator = BatchEvaluator()
    batch_evaluator.get_batch_bpp_psnr_msssim(FLAGS.original_path,
                                              FLAGS.reconstructed_path,
                                              FLAGS.compressed_path)


if __name__ == '__main__':
    tf.app.run()
