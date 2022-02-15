import numpy as np

import statcore

def test_std():
	arr = np.random.random(10000)
	npanswer = arr.std()
	myanswer = statcore.std(arr)
	assert np.isclose(npanswer, myanswer)

def test_dot():
	arr1 = np.array([1,2,3,4])
	arr2 = np.array([3,4,5,6])

	assert np.isclose(statcore.dot(arr1, arr2), np.dot(arr1, arr2))

def test_corr():
	arr1 = np.random.random(1000)
	arr2 = np.random.random(1000)

	assert np.isclose(statcore.correlation(arr1, arr2), np.corrcoef(arr1, arr2)[0][1])
