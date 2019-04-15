from matplotlib import pyplot as plt
import numpy as np
from skimage.filters import gaussian


def partialGaussian(img_arr, filter_size, sigma, mode = ['upper', 'lower']):
	upper = img_arr[: -filter_size, :, :]
	lower = img_arr[-filter_size: , :, :]

	if mode == 'upper':
		upper = gaussian(upper, sigma, multichannel = True, preserve_range = True)
	elif mode == 'lower':
		lower = gaussian(lower, sigma, multichannel = True, preserve_range = True)

	return np.concatenate((upper, lower), axis = 0)


def smoothGaussian(img_arr, y, filter_size, sigma):
	for i in range(y // filter_size):
		img_arr[: y - filter_size * i, :, :] = partialGaussian(img_arr[: y - filter_size * i, :, :], filter_size, sigma, mode = 'upper')

	for i in range((img_arr.shape[0] - y) // filter_size - 1):
		img_arr[y:img_arr.shape[0]-filter_size * i, :, :] = partialGaussian(img_arr[y: img_arr.shape[0]-filter_size * i, :, :], filter_size, sigma, mode = 'lower')
	
	return img_arr
