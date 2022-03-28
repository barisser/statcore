import time

import statcore



def test_get_shape_from_lists():
	data1 = [1]
	shape1 = statcore.get_shape_from_lists(data1)
	assert shape1 == (1,)

	data2 = [1,2,3,100]
	assert statcore.get_shape_from_lists(data2) == (4,)

	data3 = [[1,2,3], [4,5,6]]
	assert statcore.get_shape_from_lists(data3) == (2, 3)

	data4 = [data3] * 100
	assert statcore.get_shape_from_lists(data4) == (100, 2, 3)


def benchmark(func, *args, **kwargs):
	start = time.time()
	answer = func(*args, **kwargs)
	t = time.time() - start
	print("{} took {}".format(func.__name__, t))
	return t, answer

def test_tensor():
	data1 = [[[[1,2,3]] * 4]*6]*7 # 4D tensor
	tensor1 = statcore.Tensor(data1)

	assert tensor1.shape == (7, 6, 4, 3)
	assert tensor1[2, 3, 2, 1] == 2 == tensor1[2][3][2][1]

	data2 = [[[[6, 10, 15]]*4]*6]*7
	data2[2][3][3][1] = -100
	tensor2 = statcore.Tensor(data2)
	tensor3 = tensor1 + 10
	assert tensor3[2, 3, 3, 1] == 12
	assert isinstance(tensor3[1, 2], statcore.Tensor)
	assert tensor3[2, 3].values[0] == [11, 12, 13]

	tensor4 = -5 + 10 * tensor3
	assert tensor4[2, 3, 3, 1] == 115
	assert tensor1.mean() == 2
	assert (tensor1 + 3).mean() == 5
	assert tensor1.var() == 2./3
	assert (tensor1 + 3).std() == 0.816496580927726
	assert (10*tensor1).std() == 8.16496580927726


def test_generate_tensors():
	tensor1 = statcore.zeros((10, 5, 3))
	tensor2 = tensor1 + 2
	tensor3 = statcore.random((10, 5, 3))
	tensor4 = statcore.random((10, 5, 3))
	assert tensor3 != tensor4
	assert tensor2 - 2 == tensor1
	assert tensor1[3, 1, 1] == 0
	assert tensor3.std() > 0.1
