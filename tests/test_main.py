import numpy as np

import statcore

# def test_std():
# 	arr = np.random.random(10000)
# 	npanswer = arr.std()
# 	myanswer = statcore.std(arr)
# 	assert np.isclose(npanswer, myanswer)

# def test_dot():
# 	arr1 = np.array([1,2,3])
# 	arr2 = np.array([3,4,5])
# 	assert np.isclose(statcore.dot(arr1, arr2), np.dot(arr1, arr2))

# 	mat1 = np.random.random((3,4))
# 	mat2 = np.random.random((4,5))
# 	answer1 = statcore.dot(mat1, mat2)
# 	answer2 = np.dot(mat1, mat2)
# 	assert np.allclose(answer1, answer2)

# 	# 1d vs 2d cases
# 	assert np.allclose(statcore.dot(arr1, mat1), np.dot(arr1, mat1))
# 	assert np.allclose(statcore.dot(mat1.T, arr1), np.dot(mat1.T, arr1))


# def test_corr():
# 	arr1 = np.random.random(1000)
# 	arr2 = np.random.random(1000)

# 	assert np.isclose(statcore.correlation(arr1, arr2), np.corrcoef(arr1, arr2)[0][1])


# def test_lr():
# 	X = np.random.random((1000, 10))
# 	target_a = np.random.random((10))
# 	Y = np.dot(X, target_a) + np.random.random(1000) * 0.3

# 	lr = statcore.lr()
# 	lr.fit(X, Y)
# 	assert False