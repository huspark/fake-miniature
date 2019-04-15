from matplotlib import pyplot as plt
import numpy as np
from skimage.filters import gaussian


def partial_gaussian(img_arr, blurHeight, sigma, mode = ['upper', 'lower']):
	'''
	Apply a Gaussian blur to a specified part of an image array.

	Parameters:
		img_arr: ndarray
		blurHeight: int
			- the vertical length of the Gaussian filter in pixels
		sigma: float
			- the sigma value for the Gaussian blur filter
		mode: str
			- a string specifying the desired part of an image

	Returns:
		img_arr: ndarray
	'''
	# Apply a Gaussian filter to the upper part of the image
	if mode == 'upper':
		upper = img_arr[:blurHeight, :, :]
		lower = img_arr[blurHeight:, :, :]
		upper = gaussian(upper, sigma, multichannel = True, preserve_range = True)

	# Apply a Gaussian filter to the lower part of the image
	elif mode == 'lower':
		upper = img_arr[:-blurHeight, :, :]
		lower = img_arr[-blurHeight:, :, :]
		lower = gaussian(lower, sigma, multichannel = True, preserve_range = True)

	img_arr = np.concatenate((upper, lower), axis = 0)

	return img_arr


def smooth_gaussian(img_arr, y, filter_size, sigma):
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
	upper = img_arr[:y, :, :]
	lower = img_arr[y:, :, :]

	# Smoothly apply Gaussian filters to the image part above the specified y-coordinate
	for i in range(1, y // filter_size):
		blurHeight = y - filter_size * i
		upper = partial_gaussian(upper, blurHeight, sigma, mode = 'upper')

	# Smoothly apply Gaussian filters to the image part below the specified y-coordinate
	for i in range(1, (img_arr.shape[0] - y) // filter_size - 1):
		blurHeight = img_arr.shape[0] - y - filter_size * i
		lower = partial_gaussian(lower, blurHeight, sigma, mode = 'lower')

	img_arr = np.concatenate((upper, lower), axis = 0)
	
	return img_arr
