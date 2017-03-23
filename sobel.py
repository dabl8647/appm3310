#!/usr/bin/env python

# NOTE: MUST install PIL 
# http://www.pythonware.com/products/pil/

import numpy
import scipy
from scipy import ndimage
import argparse

# https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser()
parser.add_argument("imagename", help="provide file name of image want to run sobel operator")
args = parser.parse_args()

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imread.html#scipy.misc.imread
# read in image using defaults
im = scipy.misc.imread(args.imagename)

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype
# https://docs.scipy.org/doc/numpy/user/basics.types.html
# cast image array to cast to int32 type
im = im.astype('int32')

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.sobel.html
# apply sobel
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.hypot.html
mag = numpy.hypot(dx, dy)  # magnitude

mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)

scipy.misc.imsave('sobel.png', mag)
