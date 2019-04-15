from matplotlib import pyplot as plt


def get_point(img_arr):
	'''
	Take a focus point from the user.

	Parameters:
		img_arr: ndarray

	Returns:
		point: tuple
	'''
	plt.imshow(img_arr)
	plt.title("Pick a focus point.")
	point = plt.ginput(1)[0]
	plt.close()

	return point
