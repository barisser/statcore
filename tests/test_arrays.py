import statcore



def test_array():
	ar = statcore.Array([1,4,6])
	assert len(ar) == 3
	assert ar == ar
	ar2 = statcore.Array([7,8,9])
	assert ar != ar2
	assert ar + ar2 == statcore.Array([8, 12, 15])
	assert ar2 - ar == statcore.Array([6, 4, 3])
	assert ar * ar2 == statcore.Array([7, 32, 54])
	assert ar2 / ar == statcore.Array([7, 2, 1.5])
	assert ar2 % ar == statcore.Array([0, 0, 3])
	assert ar2 + 10 == statcore.Array([17, 18, 19])
	assert ar2 - 5 == statcore.Array([2, 3, 4])
	assert ar2 * 3 == statcore.Array([21, 24, 27])
	assert ar2 / 2.0 == statcore.Array([3.5, 4, 4.5])
	assert ar2 % 3 == statcore.Array([1, 2, 0])
	assert 30 * ar2 == ar2 * 30
	assert 1 + ar2 == ar2 + 1
	assert ar2 / 10 == (1/10) * ar2
	assert ar.shape == (3,)

#def test_array_dot():
