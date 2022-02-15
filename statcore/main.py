import numpy as np

def mean(array):
	"""Compute mean"""
	s = 0.
	for i in range(len(array)):
		s += array[i]
	return s / len(array)	


def variance(array):
    avg = mean(array)
    s = 0.0
    for i in range(len(array)):
        s += (array[i] - avg)**2
    return s / len(array)

def std(array):
    return variance(array)**0.5

def dot(array1, array2):
	if len(array1) != len(array2):
		raise ValueError("Arrays must be of same length")

	s = 0.
	for i in range(len(array1)):
		s += array1[i] * array2[i]
	return s

def weighted_mean(weights, array):
	return dot(weights, array)

def mae(array):
	s = 0.
	avg = mean(array)
	for i in range(len(array)):
		s += abs(array[i] - avg)
	return s / len(array)

def percentile(array, value):
	pass

def correlation(x, y):
	"""
	sum of (x-x_mean) * (y-y_mean) / ((n-1) * std(x) * std(y))
	"""
	if len(x) != len(y):
		raise RuntimeError("Arrays must be of same length")
	s = 0.
	meanx = mean(x)
	meany = mean(y)
	for i in range(len(x)):
		s += (x[i] - meanx) * (y[i] - meany)
	return s / (len(x) * std(x) * std(y))

def correlation_matrix(mat1, mat2):
	pass