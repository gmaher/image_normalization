from window_norm import multiscale_norm
import numpy as np
from scipy.ndimage import imread
import matplotlib.pyplot as plt

MIN_SCALE = 5
MAX_SCALE = 100
#im = imread('./city_small.jpeg', flatten=True)
im = np.load('./cab/192.npy')
size = np.amin(im.shape)

z = multiscale_norm(im, minimum_size=MIN_SCALE,
maximum_size=MAX_SCALE, normType='mean', post=lambda x: np.arctan(0.7*x))

plt.figure()
plt.imshow(z, cmap='gray')
plt.title('average')
plt.colorbar()
plt.savefig('./multiscale_norm.jpg',dpi=500)
plt.close()
