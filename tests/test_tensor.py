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


def test_tensor():
	data1 = [[[[1,2,3]] * 4]*6]*7 # 4D tensor
	tensor1 = statcore.Tensor(data1)

	assert tensor1.shape == (7, 6, 4, 3)
	assert tensor1[2, 3, 2, 1] == 2 == tensor1[2][3][2][1]

	data2 = [[[[6, 10, 15]]*4]*6]*7
	data2[2][3][3][1] = -100
	tensor2 = statcore.Tensor(data2)
	tensor3 = tensor1 + 10
	assert tensor3[2, 3, 3] == -90
#	assert tensor3[]
#	assert tensor3[2, 3, 4] == tensor1[2, 3, 4] + tensor2[2, 3, 4] == 10