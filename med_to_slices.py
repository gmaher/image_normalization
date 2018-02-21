from window_norm import window_norm
import numpy as np
from scipy.ndimage import imread
import matplotlib.pyplot as plt
import SimpleITK as sitk

import argparse

def resample_image(image, spacing):
    original_spacing = image.GetSpacing()
    original_size = image.GetSize()
    new_spacing = [spacing, spacing, spacing]
    new_size = [int(round(original_size[0]*(original_spacing[0]/spacing))),
                int(round(original_size[1]*(original_spacing[1]/spacing))),
                int(round(original_size[2]*(original_spacing[2]/spacing)))]

    resampled_img = sitk.Resample(image, new_size, sitk.Transform(),
                                  sitk.sitkLinear, image.GetOrigin(),
                                  new_spacing, image.GetDirection(), 0.0,
                                  image.GetPixelID())
    return resampled_img

parser = argparse.ArgumentParser()
parser.add_argument('-input')
parser.add_argument('-output')
parser.add_argument('-spacing', type=float)
args = parser.parse_args()

image = sitk.ReadImage(args.input)
image = resample_image(image, args.spacing)
im_ar = sitk.GetArrayFromImage(image)

depth = im_ar.shape[2]
for i in range(depth):
    filename = "{}/{}.npy".format(args.output,i)
    filename_jpg = "{}/{}.jpeg".format(args.output,i)

    slice_ = im_ar[i,:,:]
    np.save(filename,slice_)

    plt.figure()
    plt.imshow(slice_,cmap='gray')
    plt.colorbar()
    plt.savefig(filename_jpg,dpi=300)
    plt.close()
