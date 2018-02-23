from window_norm import multiscale_norm
import numpy as np
from scipy.ndimage import imread
import matplotlib.pyplot as plt

MIN_SCALE = 8

#im = imread('./city_small.jpeg', flatten=True)
im = np.load('./results/0082/19.npy')
size = np.amin(im.shape)

z = multiscale_norm(im, minimum_size=MIN_SCALE)

plt.figure()
plt.imshow(z, cmap='gray')
plt.title('average')
plt.colorbar()
plt.savefig('./multiscale_norm.jpg',dpi=500)
plt.close()
