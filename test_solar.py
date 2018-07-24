from window_norm import multiscale_norm, solar_norm
import numpy as np
from scipy.ndimage import imread
import matplotlib.pyplot as plt

GAMMA = 3.5
ALPHA=0.25

#im = imread('./city_small.jpeg', flatten=True)
#im = np.load('./cab/192.npy')
im = np.load('./0110/230.npy')
a0 = np.amin(im)
a1 = np.amax(im)

im_proc = 2*((1.0*im-a0)/(a1-a0))**GAMMA-1

MIN_SCALE = 5
MAX_SCALE = 100

size = np.amin(im.shape)

z = solar_norm(im, minimum_size=MIN_SCALE,
maximum_size=MAX_SCALE, normType='mean', post=lambda x: np.arctan(0.7*x))


plt.figure()
plt.imshow(z, cmap='gray')
plt.title('average')
plt.colorbar()
plt.savefig('./solar.jpg',dpi=500)
plt.close()
