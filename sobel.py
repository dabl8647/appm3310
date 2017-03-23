#!/usr/bin/env python

# NOTE: MUST install PIL
# http://www.pythonware.com/products/pil/

import argparse

# https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser()
parser.add_argument("imagename", help="provide file name of image want to run sobel operator")
args = parser.parse_args()

import numpy
import scipy
from scipy import ndimage, misc

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imread.html#scipy.misc.imread
# read in image as grayscale
im = scipy.misc.imread(args.imagename, flatten=True)

# just some basic statistics about the image
print im.dtype, im.shape

# see http://www.scipy-lectures.org/advanced/image_processing/auto_examples/plot_find_edges.html

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.sobel.html
# apply sobel
dx = ndimage.sobel(im, axis=0, mode='constant')  # horizontal derivative
dy = ndimage.sobel(im, axis=1, mode='constant')  # vertical derivative

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.hypot.html
mag = numpy.hypot(dx, dy)  # magnitude

# don't think this normalization is necessary
#mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)

# visualize

import matplotlib.pyplot as plt

plt.figure()

plt.gray() # show the filtered result in grayscale

# plotting images vertically
plt.subplot(411)
plt.imshow(im, cmap=plt.cm.gray) # note cmap=plt.cm.gray is redundant
plt.axis('off')
plt.title('Original', fontsize=14)

plt.subplot(412)
plt.imshow(dx, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Horizontal', fontsize=14)

plt.subplot(413)
plt.imshow(dy, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Vertical', fontsize=14)

plt.subplot(414)
plt.imshow(mag, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Sobel', fontsize=14)

plt.show()

# uncomment if want to save sobel image
#scipy.misc.imsave('sobel.png', mag)
