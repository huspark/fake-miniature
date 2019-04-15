from matplotlib import pyplot as plt
import numpy as np
from skimage.filters import gaussian


def partialGaussian(img_arr, filter_size, sigma, mode = ['upper', 'lower']):
	'''
	Apply a Gaussian blur to a specified part of an image array.

	Parameters:
		img_arr: ndarray
		filter_size: int
			- the vertical size of each Gaussian filter in pixels
		sigma: float
			- the sigma value for the Gaussian blur filter
		mode: str
			- a string specifying the desired part of an image

	Returns:
		img_arr: ndarray
	'''
	upper = img_arr[:-filter_size, :, :]
	lower = img_arr[-filter_size:, :, :]

	if mode == 'upper':
		upper = gaussian(upper, sigma, multichannel = True, preserve_range = True)
	elif mode == 'lower':
		lower = gaussian(lower, sigma, multichannel = True, preserve_range = True)

	img_arr = np.concatenate((upper, lower), axis = 0)

	return img_arr


def smoothGaussian(img_arr, y, filter_size, sigma):
	'''
	Smoothly apply Gaussian filters to the whole image.

	Parameters:
		img_arr: ndarray
		y: int
			- the y coordinate of the focus point specified by the user
		filter_size: int
			- the vertical size of each filter in pixels
		sigma: float
			- the sigma value for the Gaussian blur filter

	Returns:
		img_arr: ndarray
	'''
	# Smoothly apply Gaussian filters to the image part above the specified y-coordinate
	for i in range(y // filter_size):
		img_arr[:y - filter_size * i, :, :] = partialGaussian(img_arr[:y - filter_size * i, :, :], filter_size, sigma, mode = 'upper')

	# Smoothly apply Gaussian filters to the image part below the specified y-coordinate
	for i in range((img_arr.shape[0] - y) // filter_size - 1):
		img_arr[y:img_arr.shape[0] - filter_size * i, :, :] = partialGaussian(img_arr[y:img_arr.shape[0] - filter_size * i, :, :], filter_size, sigma, mode = 'lower')
	
	return img_arr
