from window_norm import window_norm
import numpy as np
from scipy.ndimage import imread
import matplotlib.pyplot as plt

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-input')
parser.add_argument('-output')
args = parser.parse_args()

MIN_SCALE = 4

if '.jpeg' in args.input or '.png' in args.input:
    im = imread(args.input, flatten=True)
elif '.npy' in args.input:
    im = np.load(args.input)
else:
    raise RuntimeError('unrecognized image format {}'.format(args.input))

size = np.amin(im.shape)

images = []

while size >= MIN_SCALE:
    print "scale {}".format(size)
    norm_im = window_norm(im,window_size=size)

    images.append(norm_im)

    plt.figure()
    plt.imshow(norm_im, cmap='gray')
    plt.title("scale {}".format(size))
    plt.colorbar()
    plt.savefig('./{}/{}.jpg'.format(args.output,size),dpi=500)
    plt.close()

    size = size/2

avg_image = np.zeros(im.shape)
for x in images: avg_image+=x/len(images)

plt.figure()
plt.imshow(avg_image, cmap='gray')
plt.title('average')
plt.colorbar()
plt.savefig('./{}/average.jpg'.format(args.output),dpi=500)
plt.close()
