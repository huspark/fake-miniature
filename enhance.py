from PIL import Image, ImageEnhance
import numpy as np


def brighten(img_arr, factor = 1.0):
	"""
	Manipulate the brightness of an input image.

	Parameters:
		img_arr: ndarray
		factor: float

	Retruns:
		img_arr: ndarray
			- the modified image array
	"""
	img = Image.fromarray(img_arr)
	enhancer = ImageEnhance.Brightness(img)
	img = enhancer.enhance(factor)
	img_arr = np.asarray(img)

	return img_arr


def saturate(img_arr, factor = 1.0):
	"""
	Manipulate the saturation of an input image.

	Parameters:
		img_arr: ndarray
		factor: float

	Retruns:
		img_arr: ndarray
			- the modified image array
	"""
	img = Image.fromarray(img_arr)
	enhancer = ImageEnhance.Color(img)
	img = enhancer.enhance(factor)
	img_arr = np.asarray(img)
	
	return img_arr
