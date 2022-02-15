import cfast as fast


def mean(array):
	"""Compute mean"""
	s = 0.
	for i in range(len(array)):
		s += array[i]
	return s / len(array)	

import numpy as np
import time

def speedtest(length):
	a = np.random.random(length)
	slowstart = time.time()
	slowmean = std(a)
	slowtime = time.time() - slowstart

	numpystart = time.time()
	numpymean = a.std()
	numpytime = time.time() - numpystart

	faststart = time.time()
	fastmean = fast.std(a)
	fasttime = time.time() - faststart

	print("{} / 1 / {}".format(slowtime / numpytime, fasttime / numpytime))

