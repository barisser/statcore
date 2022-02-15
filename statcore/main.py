

def mean(array):
	"""Compute mean"""
	s = 0.
	for i in range(len(array)):
		s += array[i]
	return s / len(array)	


import numpy as np
import time

a = np.random.random(100000)

b = time.time()
r = mean(a)
z = time.time() - b
print(z)

b = time.time()
q = a.mean()
w = time.time()-b

print(w)
print(z/w)

import pdb;pdb.set_trace()

# def std(array):
# 	"""
# 	Compute standard deviation.
# 	"""

