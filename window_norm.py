import numpy as np
from scipy.ndimage.filters import gaussian_filter
EPS = 1e-3

def do_nothing(x):
    return x

def solar_norm(x,minimum_size=8, maximum_size=80, normType='mean', post=lambda x: np.arctan(0.7*x),
    gamma=3.5, alpha=0.5):

    z = multiscale_norm(x,minimum_size,maximum_size,normType,post)

    a0 = np.amin(x)
    a1 = np.amax(x)

    im_proc = 2*((1.0*x-a0)/(a1-a0))**gamma-1

    im = alpha*im_proc+(1-alpha)*z
    return im.copy()

def multiscale_norm(x,minimum_size=4, maximum_size=40, normType='mean', post=do_nothing):
    images = []
    size = maximum_size
    while size >= minimum_size:
        norm_im = window_norm(x,window_size=size)
        norm_im = post(norm_im)

        images.append(norm_im)

        size = size/2

    if normType == 'mean':
        avg_image = np.zeros(x.shape)
        for im in images: avg_image+=im/len(images)
        return avg_image.copy()

    elif normType == 'max':
        stack = np.amax(np.array(images),axis=0)
        return stack

# def window_norm(x,window_size):
#     counts = np.zeros(x.shape)
#     z      = np.zeros(x.shape)
#
#     start = 0
#     x_end = x.shape[0]-window_size+1
#     y_end = x.shape[1]-window_size+1
#
#     for j in range(start, y_end):
#         for i in range(start, x_end):
#             j_end = j+window_size
#             i_end = i+window_size
#
#             counts[i:i_end,j:j_end]+=1
#
#             x_curr   = x[i:i_end,j:j_end]
#             mu_curr  = np.mean(x_curr)
#             std_curr = np.std(x_curr)
#
#             z[i:i_end,j:j_end] += (1.0*x_curr-mu_curr)/(std_curr+EPS)
#
#     z = z/counts
#     return z.copy()

def window_norm(x,window_size):
    sigma = window_size
    mu = gaussian_filter(1.0*x,sigma,truncate=3.0)
    var = gaussian_filter((1.0*x-mu)**2,sigma,truncate=3.0)
    std = np.sqrt(var)
    z = (x-mu)/(std+EPS)
    return z.copy()
