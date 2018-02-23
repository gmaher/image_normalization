import numpy as np
from scipy.ndimage.filters import gaussian_filter
EPS = 1e-3

def multiscale_norm(x,minimum_size=8, type='mean'):
    images = []
    size = np.amin(x.shape)
    while size >= minimum_size:
        norm_im = window_norm(x,window_size=size)

        images.append(norm_im)

        size = size/2

    avg_image = np.zeros(x.shape)
    for im in images: avg_image+=im/len(images)

    return avg_image.copy()

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
