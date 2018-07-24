from window_norm import multiscale_norm
import numpy as np
from scipy.ndimage import imread
import matplotlib.pyplot as plt

GAMMA = 3.5

#im = imread('./city_small.jpeg', flatten=True)
im = np.load('./cab/192.npy')
a0 = np.amin(im)
a1 = np.amax(im)

im_proc = 2*((1.0*im-a0)/(a1-a0))**GAMMA-1


plt.figure()
plt.imshow(im_proc, cmap='gray')
plt.title('average')
plt.colorbar()
plt.savefig('./gamma_norm.jpg',dpi=500)
plt.close()
