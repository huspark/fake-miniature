import sys
import argparse

import matplotlib.pyplot as plt
import numpy as np
from skimage import io

from core import *
from enhance import *
from process import *


def process_arg():
	'''
	Process the user input.

	Parameters:
		None

	Returns:
		args: argparse.Namespace()
	'''
	parser = argparse.ArgumentParser(description = "This program manipulates creates a miniature scene of an input image.")
	parser.add_argument('-f', '--filename', type = str, required = True,  help = 'the input file name')
	parser.add_argument('-s', '--filter_size', type = int, required = False,  help = 'the vertical size of each Gaussian filter in pixels')
	parser.add_argument('-r', '--filter_radius', type = float, required = False,  help = 'the sigma value for the first Gaussian blur filter')
	parser.add_argument('-b', '--brighten_factor', default = 1.1, type = float, required = False,  help = 'the constant for a brightening effect')
	parser.add_argument('-c', '--saturate_factor', default = 1.5, type = float, required = False,  help = 'the constant for a saturation effect')

	args = parser.parse_args()

	return args


if __name__ == '__main__':
	# Process arguments
	args = process_arg()

	# Check if the specified file exists
	try:
		img = io.imread(args.filename)
	except FileNotFoundError:
		sys.exit("Error: File not found")

	# If filter size is not specified, use (image height / 20)
	if args.filter_size == None:
		args.filter_size = img.shape[0] // 20

	# If filter_radius is not specified, use 1 + img.shape[0] ** 2 * 0.0000001
	if args.filter_radius == None:
		args.filter_radius = 1 + img.shape[0] ** 2 * 0.0000001

	# Print out the values of the parameters being used
	print('filter_size =', args.filter_size)
	print('filter_radius =', args.filter_radius)
	print('brighten_factor =', args.brighten_factor)
	print('saturate_factor =', args.saturate_factor)

	# Take a focus point from the user
	focus_point = get_point(img)

	# Enhance the input image
	img = brighten(img, factor = args.brighten_factor)
	img = saturate(img, factor = args.saturate_factor)

	# Apply blurs to the enhanced image
	img = img.astype(np.float64)
	out = smooth_gaussian(img, y = int(focus_point[1]), filter_size = args.filter_size, sigma = args.filter_radius)
	out = out.astype(dtype = np.uint8)

	# Save and display the output image
	io.imsave(fname = ''.join(args.filename.split('.')[:-1]) + '_out.jpg', arr = out)
	plt.imshow(out)
	plt.title('Output')
	plt.show()
	